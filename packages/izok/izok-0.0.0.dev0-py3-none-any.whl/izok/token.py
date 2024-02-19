#  --------------------------------------------------------------------------------
#  Izok: A modeling system similar to GAMS for pyomo.
#  Copyright 2024,  Andrey Sergeevich Storozhenko, All rights reserved.
#  This software is distributed under the 3-clause BSD License.
#  --------------------------------------------------------------------------------

from sys import intern
from .position import Position

TOKEN_WHITE_SPACE = intern("whitespace")
TOKEN_NEW_LINE = intern("newline")
TOKEN_COMMENT = intern("comment")
TOKEN_IDENT = intern("ident")
TOKEN_LABEL = intern("label")
TOKEN_NUMBER = intern("number")

TOKEN_LPAREN = intern("lparen")
TOKEN_RPAREN = intern("rparen")
TOKEN_OPERATOR = intern("operator")
TOKEN_BAD_SYMBOL = intern("badsymbol")
TOKEN_END = intern("end")
TOKEN_SEMICOLON = intern("semicolon")
TOKEN_POINTPOINT = intern("pointpoint")
TOKEN_DOLLAR = intern("dollar")
TOKEN_EQNTYPE = intern("eqntype")
TOKEN_COMMA = intern("comma")


class Token:
    def __init__(self, pos: Position, type_str: str, value: str):
        self.pos = pos
        self.type = type_str
        self.value = value

    def __str__(self) -> str:
        if self.type == TOKEN_NEW_LINE or self.type == TOKEN_END:
            return f"[{self.pos.pos},{self.pos.line}] {self.type}"
        elif self.type == TOKEN_WHITE_SPACE:
            return f"[{self.pos.pos},{self.pos.line}] {self.type} symbol count {len(self.value)}"
        return f"[{self.pos.pos},{self.pos.line}] {self.type} {self.value}"
