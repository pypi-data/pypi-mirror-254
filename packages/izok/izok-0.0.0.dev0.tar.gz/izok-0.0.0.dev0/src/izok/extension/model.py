#  --------------------------------------------------------------------------------
#  Izok: A modeling system similar to GAMS for pyomo.
#  Copyright 2024,  Andrey Sergeevich Storozhenko, All rights reserved.
#  This software is distributed under the 3-clause BSD License.
#  --------------------------------------------------------------------------------

from typing import Union, Callable, List
from pyomo.environ import *
from .domain import Domain
from izok.ast_est import AST
from izok.error import error
from izok.errorid import *


def get_property_by_name(model: Model, domain: Union[Domain, None], ast: AST,  ident: str):
    if domain is not None and ident in domain:
        return domain.get_set_value(ident)
    else:
        try:
            return getattr(model, ident)
        except AttributeError:
            error(ast.pos,
                  GEN_PROPERTY_NAME_ERROR,
                  "Error in model property name",
                  f"Error in model property name: {ident}")


def is_set(obj):
    return isinstance(obj, Set)


def get_set(model: Model, ast: AST, property_name: str) -> Union[Set, None]:
    prp_set = get_property_by_name(model, None, ast, property_name)

    if is_set(prp_set):
        return prp_set.value
    else:
        return None


def check_index_or_call(obj) -> bool:
    if isinstance(obj, Var) or isinstance(obj, Param):
        return True
    elif isinstance(obj, Callable):
        return False
    else:
        Exception("Panic. Object not indexing and can be called.")


def skip_constraint():
    return Constraint.Skip


def init_constraint(model: Model, ast: AST, domain: [List[str], None], ident: str, eq: Callable):
    if domain is None:
        setattr(model, ident, Constraint(rule=eq))
    else:
        domain_lst = []
        for set_name in domain:
            domain_lst.append(get_set(model, ast, set_name))

        setattr(model, ident, Constraint(*domain_lst, rule=eq))


def init_objective(model: Model, ast: AST, ident: str, sense: str, obj: Callable):
    if sense == 'MAXIMIZE':
        setattr(model, ident, Objective(rule=obj, sense=maximize))
    else:
        setattr(model, ident, Objective(rule=obj, sense=minimize))
