#  --------------------------------------------------------------------------------
#  Izok: A modeling system similar to GAMS for pyomo.
#  Copyright 2024,  Andrey Sergeevich Storozhenko, All rights reserved.
#  This software is distributed under the 3-clause BSD License.
#  --------------------------------------------------------------------------------

from typing import Union
from izok.extension.domain import Domain
from .position import Position


class AST:
    def __init__(self, pos: Position):
        self.pos = pos

    def to_est(self) -> Union['EST', None]:
        raise Exception("Must be override")


class EST:
    def __init__(self, ast: AST):
        self.ast = ast

    def __call__(self, model, domain: Domain):
        pass

    def __str__(self):
        return str(self.ast)
