#  --------------------------------------------------------------------------------
#  Izok: A modeling system similar to GAMS for pyomo.
#  Copyright 2024,  Andrey Sergeevich Storozhenko, All rights reserved.
#  This software is distributed under the 3-clause BSD License.
#  --------------------------------------------------------------------------------

class Position:
    def __init__(self, source: str, line: int, pos: int = 0, offset: int = 0):
        self.source = source
        self.line = line
        self.pos = pos
        self.offset = offset
