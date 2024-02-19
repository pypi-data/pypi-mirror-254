#  --------------------------------------------------------------------------------
#  Izok: A modeling system similar to GAMS for pyomo.
#  Copyright 2024,  Andrey Sergeevich Storozhenko, All rights reserved.
#  This software is distributed under the 3-clause BSD License.
#  --------------------------------------------------------------------------------

from typing import Union
from izok.ast_est import AST, EST
from izok.baseparser import ParserRule, BaseParser
from izok.token import *
from izok.errorid import *
from .domain import Domain
from .model import init_objective


class ObjectiveAST(AST):
    def __init__(self, pos: Position, name: str, sense: str, expr: AST):
        super(ObjectiveAST, self).__init__(pos)
        self.name = name
        self.sense = sense
        self.expr = expr

    def __str__(self):
        return f"obj {self.sense} {self.name} .. {self.expr} ;"

    def to_est(self) -> Union['EST', None]:
        return ObjectiveEST(self, self.name, self.sense, self.expr.to_est())


class ObjectiveEST(EST):
    def __init__(self, ast: AST, ident: str, sense: str, expr: EST):
        super(ObjectiveEST, self).__init__(ast)
        self.ident = ident
        self.sense = sense
        self.expr = expr

    def __call__(self, model, *args):
        domain = Domain()
        return self.expr(model, domain)

    def init(self, model):
        init_objective(model, self.ast, self.ident, self.sense, self)


class ObjectiveRule(ParserRule):
    def __init__(self):
        super(ObjectiveRule, self).__init__("obj")

    def parse(self, parser: BaseParser) -> AST:
        # obj maximize | minimize name .. expr ;
        pos = parser.scaner.token.pos
        parser.scan()
        sense = parser.expect(TOKEN_IDENT).value.upper()
        if sense not in ['MAXIMIZE', 'MINIMIZE']:
            parser.error(PARSER_OBJ_SENSE_ERROR,
                         "Wrong name of objective sense.",
                         f"Dont specify sense. Must be MINIMIZE or MAXIMIZE but get: {sense}.")
        name = parser.expect(TOKEN_IDENT).value
        parser.expect(TOKEN_POINTPOINT)
        expr = parser.expr()
        parser.expect(TOKEN_SEMICOLON)
        return ObjectiveAST(pos, name, sense, expr)

    def skip_block(self, parser: BaseParser) -> None:
        parser.skip_to_semicolon_and_skip()
