
#  --------------------------------------------------------------------------------
#  Izok: A modeling system similar to GAMS for pyomo.
#  Copyright 2024,  Andrey Sergeevich Storozhenko, All rights reserved.
#  This software is distributed under the 3-clause BSD License.
#  --------------------------------------------------------------------------------

def build(model, text: str):
    from .parser import Parser
    parser = Parser(text)
    while True:
        ast = parser.parse()
        if ast is None:
            break

        est = ast.to_est()
        est.init(model)


__version__ = "0.0.0.dev0"
