#  --------------------------------------------------------------------------------
#  Izok: A modeling system similar to GAMS for pyomo.
#  Copyright 2024,  Andrey Sergeevich Storozhenko, All rights reserved.
#  This software is distributed under the 3-clause BSD License.
#  --------------------------------------------------------------------------------

from typing import Union, List
from izok.ast_est import AST, EST
from izok.ast import OperandAST, IdentListAST, ExprAST
from izok.baseparser import ParserRule, BaseParser
from izok.token import *
from .domain import Domain
from .model import init_constraint, skip_constraint


class EquationAST(AST):
    def __init__(self,
                 pos: Position, name: str,
                 domain: Union[AST, None],
                 expr: AST):
        super(EquationAST, self).__init__(pos)
        self.name = name
        self.domain = domain
        self.expr = expr

    def __str__(self):
        return f"{self.name} {'' if self.domain is None else self.domain} .. {self.expr} ;"

    def to_est(self) -> Union[EST, None]:
        if isinstance(self.domain, OperandAST):
            domain = self.domain.expr
            cond = self.domain.cond.to_est()
        else:
            domain = self.domain
            cond = None

        if isinstance(domain, IdentListAST):
            return EquationEST(self, self.name, domain.idents, cond, self.expr.to_est())
        else:
            return EquationEST(self, self.name, domain, cond, self.expr.to_est())


class EquationEST(EST):
    def __init__(self, ast: AST, ident: str, domain: Union[List[str], None], cond: Union[EST, None], expr: EST):
        super(EquationEST, self).__init__(ast)
        self.ident = ident
        self.domain = domain
        self.cond = cond
        self.expr = expr

    def __call__(self, model, *args):
        domain = Domain()
        if self.domain is None:
            return self.expr(model, domain)
        else:
            # init domain from args
            if self.cond is not None:
                if self.cond(model, domain):
                    return self.expr(model, domain)
                else:
                    return skip_constraint()
            else:
                return self.expr(model, domain)

    def init(self, model):
        init_constraint(model, self.ast, self.domain, self.ident, self)


class EquationRule(ParserRule):
    def __init__(self):
        super(EquationRule, self).__init__("equation")

    def parse(self, parser: BaseParser) -> AST:
        # name domain.. expr eq_type expr ;

        name = parser.scaner.token.value
        pos = parser.scaner.token.pos
        parser.scan()

        domain = parser.domain()

        parser.expect(TOKEN_POINTPOINT)
        left = parser.expr()
        eq_type = parser.expect(TOKEN_EQNTYPE)
        right = parser.expr()

        parser.expect(TOKEN_SEMICOLON)
        return EquationAST(pos, name, domain, ExprAST(eq_type.pos, eq_type.value, left, right))

    def skip_block(self, parser: BaseParser) -> None:
        parser.skip_to_semicolon_and_skip()
