#  --------------------------------------------------------------------------------
#  Izok: A modeling system similar to GAMS for pyomo.
#  Copyright 2024,  Andrey Sergeevich Storozhenko, All rights reserved.
#  This software is distributed under the 3-clause BSD License.
#  --------------------------------------------------------------------------------

from typing import Union, List
from izok.extension.domain import Domain
from .errorid import *
from .error import error
from .extension.model import get_property_by_name, check_index_or_call
from .ast_est import AST, EST


_bin_op_lambda = {
    "+": lambda left, right: left + right,
    "-": lambda left, right: left - right,
    "/": lambda left, right: left / right,
    "*": lambda left, right: left * right,
    "**": lambda left, right: left ** right,
    "<>": lambda left, right: left != right,
    ">": lambda left, right: left > right,
    ">=": lambda left, right: left >= right,
    "<": lambda left, right: left < right,
    "<=": lambda left, right: left <= right,
    "=": lambda left, right: left == right,
    "=e=": lambda left, right: left == right,
    "=l=": lambda left, right: left <= right,
    "=g=": lambda left, right: left >= right,
    "and": lambda left, right: bool(left) and bool(right),
    "or": lambda left, right: bool(left) or bool(right),
    "xor": lambda left, right: bool(left) != bool(right),
}

_un_op_lambda = {
    "+": lambda l, r: r,
    "-": lambda l, r: - r,
    "not": lambda l, r: not bool(r),
}


class OperandEST(EST):
    def __init__(self, ast: AST, expr: EST, cond: Union[EST, None]):
        super(OperandEST, self).__init__(ast)
        self.expr = expr
        self.cond = cond

    def __call__(self, model, domain: Domain):
        if self.cond is not None:
            cond_value = self.cond(model, domain)
            try:
                cond_value = bool(cond_value)
            except Exception as err:
                error(
                    self.ast.pos,
                    GEN_TYPE_CONVERT_ERROR,
                    "Unable to reduce expression to boolean type.",
                    str(err)
                )
            if cond_value:
                return self.expr(model, domain)
            else:
                return 0
        else:
            return self.expr(model, domain)

#    def __str__(self):
#        if self.cond is None:
#            return f"{str(self.expr.ast)}"
#        else:
#            return f"{str(self.expr.ast)}${str(self.cond.ast)}"


class ExprEST(EST):
    def __init__(self, ast: AST, value: str, left: Union[EST, None], right: EST):
        super(ExprEST, self).__init__(ast)
        global _un_op_lambda, _bin_op_lambda
        self.ast = ast
        self.left = left
        self.right = right
        self.value = value
        if self.left is None:
            self.op = _un_op_lambda[value]
        else:
            self.op = _bin_op_lambda[value]

    def __call__(self, model, domain: Domain):
        left = None
        if self.left is not None:
            if isinstance(self.left, EST):
                left = self.left(model, domain)
            else:
                left = self.left
        if isinstance(self.right, EST):
            right = self.right(model, domain)
        else:
            right = self.right

        try:
            return self.op(left, right)
        except Exception as err:
            if self.left is None:
                error(self.right.ast.pos,
                      GEN_OPERATOR_ERROR,
                      f"Bad operand type for unary {self.value}: {type(right)}",
                      f"{err}")
            else:
                error(self.left.ast.pos,
                      GEN_OPERATOR_ERROR,
                      f"Unsupported operand type(s) for {self.value}: {type(left)} and {type(right)}",
                      f"{err}")

#    def __str__(self):
#        if self.left is None:
#            return f"[{self.value} {str(self.right.ast)}]"
#        else:
#            return f"[{str(self.right.ast)} {self.value} {str(self.left.ast)}]"


class IdentEST(EST):
    def __init__(self, ast: AST, ident: str):
        super(IdentEST, self).__init__(ast)
        self.ident = ident

#    def __str__(self):
#        return self.ident

    def __call__(self, model, domain: Domain):
        return get_property_by_name(model, domain, self.ast, self.ident)


class LabelEST(EST):
    def __init__(self, ast: AST, value: str):
        super(LabelEST, self).__init__(ast)
        self.value = value

#    def __str__(self):
#        return self.value

    def __call__(self, model, domain: Domain):
        return self.value


class NumberEST(EST):
    def __init__(self, ast: AST, value: str):
        super(NumberEST, self).__init__(ast)
        self.value = value

#    def __str__(self):
#        return self.value

    def __call__(self, model, domain: Domain):
        return float(self.value)


class ExprListEST(EST):
    def __init__(self, ast: AST, expr_list: List[EST]):
        super(ExprListEST, self).__init__(ast)
        self.expr_list = expr_list

#    def __str__(self):
#        if len(self.expr_list) == 1:
#            return f"{self.expr_list[0].ast}"
#        else:
#           return f"{','.join(str(e.ast) for e in self.expr_list)}"

    def __call__(self, model, domain: Domain):
        return [expr(model, domain) for expr in self.expr_list]


class SetListEST(EST):
    def __init__(self, ast: AST, idents: List[str]):
        super(SetListEST, self).__init__(ast)
        self.idents = idents

#    def __str__(self):
#        return str(self.ast)

    def __call__(self, model, domain: Domain):
        return [get_property_by_name(model, domain, self.ast, ident) for ident in self.idents]


class FunctionEST(EST):
    def __init__(self, ast: AST, ident: str, args: EST):
        super(FunctionEST, self).__init__(ast)
        self.ident = ident
        self.args = args

    def __call__(self, model, domain):
        prp = get_property_by_name(model, domain, self.ast, self.ident)
        args = self.args(model, domain)
        if check_index_or_call(prp):
            try:
                return prp.__getitem__(*args)
            except Exception as err:
                error(self.ast,
                      GEN_INDEXING_ERROR,
                      "Can't execute index operation",
                      str(err))
        else:
            try:
                return prp(*args)
            except Exception as err:
                error(self.ast,
                      GEN_INDEXING_ERROR,
                      "Can't call function",
                      str(err))
