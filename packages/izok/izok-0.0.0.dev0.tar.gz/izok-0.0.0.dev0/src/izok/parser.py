#  --------------------------------------------------------------------------------
#  Izok: A modeling system similar to GAMS for pyomo.
#  Copyright 2024,  Andrey Sergeevich Storozhenko, All rights reserved.
#  This software is distributed under the 3-clause BSD License.
#  --------------------------------------------------------------------------------

from .baseparser import BaseParser
from .extension.objective import ObjectiveRule
from .extension.equation import EquationRule
#from izok.extension.sum import SumFunctionRule


class Parser(BaseParser):
    def __init__(self, text: str):
        super(Parser, self).__init__(text,
                                     [
                                        ObjectiveRule()
                                     ], EquationRule(),
                                     [
                                         #SumFunctionRule()
                                     ])
