#  --------------------------------------------------------------------------------
#  Izok: A modeling system similar to GAMS for pyomo.
#  Copyright 2024,  Andrey Sergeevich Storozhenko, All rights reserved.
#  This software is distributed under the 3-clause BSD License.
#  --------------------------------------------------------------------------------

from .ast import *
from .scaner import Scaner, un_op_names, operator_priority
from .token import *
from .error import IzokException, error, set_base_position
from .errorid import *


class ParserRule:
    def __init__(self, ident: str):
        self.ident = ident

    def act_parse(self, parser) -> AST:
        set_base_position(parser.scaner.token.pos)
        ast = self.parse(parser)
        set_base_position(None)
        return ast

    def parse(self, parser) -> AST:
        raise Exception("Must be overriden")

    def skip_block(self, parser) -> None:
        raise Exception("Must be overriden")


class FunctionRule:
    def __init__(self, ident: str):
        self.ident = ident

    def parse(self, parser, ident: Token) -> AST:
        raise Exception("Must be overriden")


class BaseParser:
    def __init__(self, text: str,
                 rules: List[ParserRule], default_rule: ParserRule = None,
                 function_rules: List[FunctionRule] = None):
        self.scaner = Scaner(text)
        self._rules = dict()
        for rule in rules:
            self._rules[rule.ident.upper()] = rule
        self._default_rule = default_rule
        self._function_rules = dict()
        if function_rules is not None:
            for function_rule in function_rules:
                self._function_rules[function_rule.ident.upper()] = function_rule

    def error(self, error_id: int, head_msg: str, tile_msg: str, base_token: Union[Token, None] = None) -> None:
        if base_token is None:
            error(self.scaner.token.pos, error_id, head_msg, tile_msg)
        else:
            error(base_token.pos, error_id, head_msg, tile_msg)

    def scan(self) -> None:

        def step():
            self.scaner.scan()
            bad_chars = ""
            token_begin = None
            while self.scaner.token.type == "":
                if token_begin is None:
                    token_begin = self.scaner.token
                bad_chars += self.scaner.token.value
                self.scaner.scan()
            if bad_chars != "":
                self.error(PARSER_EXPECT_EXCEPTION,
                           "Bad chars",
                           f"Bad chars {bad_chars}", token_begin)

        step()
        while self.case(TOKEN_WHITE_SPACE, TOKEN_NEW_LINE):
            step()

    def case(self, *tokens: str) -> bool:
        return any(self.scaner.token.type == t for t in tokens)

    def expect(self, *tokens: str) -> Token:
        if not any(self.scaner.token.type == token for token in tokens):
            self.error(PARSER_EXPECT_EXCEPTION,
                       "Unexpected token",
                       f"Expect {','.join(token.upper() for token in tokens)} " +
                       f"but got {self.scaner.token.type.upper()}")
        ret = self.scaner.token
        self.scan()
        return ret

    def skip_to_semicolon_and_skip(self) -> None:
        while not self.case(TOKEN_SEMICOLON, TOKEN_END):
            self.scan()
        if self.case(TOKEN_SEMICOLON):
            self.scan()

    def parse(self) -> Union[AST, None]:
        if self.scaner.token is None:
            self.scan()

        if self.case(TOKEN_END):
            return None

        if self.case(TOKEN_IDENT):
            rule = self._rules.get(self.scaner.token.value.upper(), None)
            if rule is None:
                if self._default_rule is None:
                    self.error(PARSER_MATCH_RULE_EXCEPTION,
                               "Rules key error.",
                               f"The identifier name ({self.scaner.token.value}) does not match any rules.")
                else:
                    try:
                        return self._default_rule.act_parse(self)
                    except IzokException as err:
                        self._default_rule.skip_block(self)
                        print(err)
            else:
                try:
                    return rule.act_parse(self)
                except IzokException as err:
                    rule.skip_block(self)
                    print(err)
        else:
            self.expect(TOKEN_IDENT)
        return None

    def expr(self) -> AST:
        stack = []
        line = []

        if self.case(TOKEN_OPERATOR):
            if not (self.scaner.token.value in un_op_names):
                self.error(PARSER_NOT_UNARY_OPERATOR,
                           "The operator is not a unary operator.",
                           f"The {self.scaner.token.value.upper()} operator is not unary.")
            opr = self.scaner.token
            self.scan()
            line.append(
                ExprAST(opr.pos, opr.value, None, self.operand()))
        else:
            line.append(self.operand())

        while self.case(TOKEN_OPERATOR):
            pr = operator_priority[self.scaner.token.value]
            if len(stack) != 0:
                op1, pr1 = stack[-1]
                if abs(pr) > abs(pr1):
                    stack.pop(-1)
                    if pr1 < 0:
                        line.append(
                            ExprAST(op1.pos, op1.value, None, line.pop(-1)))
                    else:
                        right_op = line.pop(-1)
                        left_op = line.pop(-1)
                        line.append(ExprAST(op1.pos, op1.value, left_op, right_op))
            stack.append((self.scaner.token, pr))
            self.scan()
            line.append(self.operand())

        while len(stack) != 0:
            op, _ = stack.pop(-1)
            right_op = line.pop(-1)
            left_op = line.pop(-1)
            line.append(ExprAST(op.pos, op.value, left_op, right_op))

        return line[0]

    def operand(self) -> AST:
        cond = None
        base = self._prim_operand()
        if self.case(TOKEN_DOLLAR):
            self.scan()
            cond = self.expr()
        if cond is None:
            return base
        else:
            return OperandAST(base, cond)

    def _prim_operand(self) -> AST:
        ret = self.sub_expr()
        if ret is None:
            ret = self.lit()
            if ret is None:
                ret = self.ident()
                if ret is None:
                    if self.scaner.token.value == '\n':
                        end = "END_OF_LINE"
                    elif self.scaner.token.value == '\0':
                        end = "END_OF_STRING"
                    else:
                        end = self.scaner.token.value
                    self.error(PARSER_EXPECT_EXCEPTION,
                               "Unexpected token",
                               f"Expect ( or NUMBER or LABEL or IDENT but got {end}"
                               )
        return ret

    def expr_list(self) -> ExprListAST:
        expr_list = []
        expr = self.expr()
        expr_list.append(expr)
        while self.case(TOKEN_COMMA):
            self.scan()
            expr_list.append(self.expr())
        return ExprListAST(expr_list[0].pos, expr_list)

    def ident(self) -> Union[AST, None]:
        if self.case(TOKEN_IDENT):
            ident = self.scaner.token
            self.scan()
            if self.case(TOKEN_LPAREN):
                self.scan()

                function_rule = self._function_rules.get(ident.value.upper(), None)

                if function_rule is None:
                    expr_list = self.expr_list()
                    self.expect(TOKEN_RPAREN)
                    return FunctionAST(ident.pos, ident.value, expr_list)
                else:
                    ret = function_rule.parse(self, ident)
                    self.expect(TOKEN_RPAREN)
                    return ret
            return IdentAST(ident.pos, ident.value)
        return None

    def lit(self) -> Union[NumberAST, LabelAST, None]:
        if self.case(TOKEN_NUMBER, TOKEN_LABEL):
            if self.scaner.token.type == TOKEN_LABEL:
                ret = LabelAST(self.scaner.token.pos, self.scaner.token.value)
            else:
                ret = NumberAST(self.scaner.token.pos, self.scaner.token.value)
            self.scan()
            return ret
        return None

    def sub_expr(self) -> Union[AST, None]:
        if self.case(TOKEN_LPAREN):
            lbr = self.scaner.token
            self.scan()
            if self.case(TOKEN_RPAREN):
                expr = None
            else:
                expr = self.expr()
            self.expect(TOKEN_RPAREN)
            return SubExprAST(lbr.pos, expr)
        else:
            return None

    def domain(self) -> Union[AST, None]:
        cond = None
        if self.case(TOKEN_IDENT):
            base = IdentAST(self.scaner.token.pos, self.scaner.token.value)
            self.scan()
        elif self.case(TOKEN_LPAREN):
            pos = self.scaner.token.pos
            self.scan()
            if self.case(TOKEN_RPAREN):
                base = IdentListAST(pos, [])
            else:
                idents = [self.expect(TOKEN_IDENT).value]
                while self.case(TOKEN_COMMA):
                    self.scan()
                    idents.append(self.expect(TOKEN_IDENT).value)
                base = IdentListAST(pos, idents)
                self.expect(TOKEN_RPAREN)
        else:
            return None

        if self.case(TOKEN_DOLLAR):
            self.scan()
            cond = self.expr()

        if cond is None:
            return base
        else:
            return OperandAST(base, cond)
