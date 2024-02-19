#  --------------------------------------------------------------------------------
#  Izok: A modeling system similar to GAMS for pyomo.
#  Copyright 2024,  Andrey Sergeevich Storozhenko, All rights reserved.
#  This software is distributed under the 3-clause BSD License.
#  --------------------------------------------------------------------------------

from .position import Position
from .est import *


class IdentAST(AST):
    def __init__(self,  pos: Position, ident: str):
        super(IdentAST, self).__init__(pos)
        self.ident = ident

    def __str__(self):
        return self.ident

    def to_est(self) -> Union[EST, None]:
        return IdentEST(self, self.ident)


class LabelAST(AST):
    def __init__(self,  pos: Position, value: str):
        super(LabelAST, self).__init__(pos)
        self.value = value

    def __str__(self):
        return f"'{self.value}'"

    def to_est(self) -> Union[EST, None]:
        return LabelEST(self, self.value)


class NumberAST(AST):
    def __init__(self,  pos: Position, value: str):
        super(NumberAST, self).__init__(pos)
        self.value = value

    def __str__(self):
        return self.value

    def to_est(self) -> Union[EST, None]:
        return NumberEST(self, self.value)


class ExprAST(AST):
    def __init__(self, pos: Position, value: str, left_op: Union[AST, None], right_op: AST):
        super(ExprAST, self).__init__(pos)
        self.value = value
        self.left = left_op
        self.right = right_op

    def __str__(self):
        if self.left is None:
            return f"[{self.value} {str(self.right)}]"
        else:
            return f"[{str(self.left)} {self.value} {str(self.right)}]"

    def to_est(self) -> Union[EST, None]:
        if self.left is None:
            return ExprEST(self, self.value, None, self.right.to_est())
        else:
            return ExprEST(self, self.value, self.left.to_est(), self.right.to_est())


class OperandAST(AST):
    def __init__(self, expr: AST, cond: Union[AST, None]):
        super(OperandAST, self).__init__(expr.pos)
        self.expr = expr
        self.cond = cond

    def __str__(self):
        return f"{self.expr}{'' if self.cond is None else '$'+str(self.cond)}"

    def to_est(self) -> Union[EST, None]:
        if self.cond is None:
            return OperandEST(self, self.expr.to_est(), None)
        else:
            return OperandEST(self, self.expr.to_est(), self.cond.to_est())


class SubExprAST(AST):
    def __init__(self, pos: Position, expr: Union[AST, None]):
        super(SubExprAST, self).__init__(pos)
        self.expr = expr

    def __str__(self):
        return f"({'' if self.expr is None else self.expr})"

    def to_est(self) -> Union[EST, None]:
        if self.expr is None:
            return None
        else:
            return self.expr.to_est()


class IdentListAST(AST):
    def __init__(self, pos: Position, idents: List[str]):
        super(IdentListAST, self).__init__(pos)
        self.idents = idents

    def __str__(self):
        if len(self.idents) == 1:
            return f"{self.idents[0]}"
        else:
            return f"({','.join(str(x) for x in self.idents)})"

    def to_est(self) -> Union[EST, None]:
        return SetListEST(self, self.idents)


class ExprListAST(AST):
    def __init__(self, pos: Position, expr_list: List[AST]):
        super(ExprListAST, self).__init__(pos)
        self.expr_list = expr_list

    def __str__(self):
        if len(self.expr_list) == 1:
            return f"{self.expr_list[0]}"
        else:
            return f"{','.join(str(x) for x in self.expr_list)}"

    def to_est(self) -> Union[EST, None]:
        expr_list = []
        for expr in self.expr_list:
            expr_est = expr.to_est()
            if expr_est is None:
                error(expr.pos,
                      GEN_ESP_NONE_ERROR,
                      "Convert to a EST error",
                      "When converted to a EST, the result is None"
                      )
            expr_list.append(expr_est)

        return ExprListEST(self, expr_list)


class FunctionAST(AST):
    def __init__(self, pos: Position, ident: str, args: Union[IdentListAST, ExprListAST]):
        super(FunctionAST, self).__init__(pos)
        self.ident = ident
        self.args = args

    def __str__(self):
        return f"{self.ident}({self.args})"

    def to_est(self) -> Union[EST, None]:
        return FunctionEST(self, self.ident, self.args.to_est())
