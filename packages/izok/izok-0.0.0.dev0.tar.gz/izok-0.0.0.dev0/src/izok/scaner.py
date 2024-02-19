#  --------------------------------------------------------------------------------
#  Izok: A modeling system similar to GAMS for pyomo.
#  Copyright 2024,  Andrey Sergeevich Storozhenko, All rights reserved.
#  This software is distributed under the 3-clause BSD License.
#  --------------------------------------------------------------------------------

from typing import Union
import re
from .token import *
from .basescaner import ScanerRule, BaseScaner

# parser regular expressions
white_space_re = re.compile(r" +")
new_line_re = re.compile(r"(\r\n|\r|\n)")

comment_re = re.compile(r"#(.*)")
ident_re = re.compile(r"(\w+)")
label_re = re.compile(r"'([^'\r\n]*)['\r\n]")
number_re = re.compile(r"(\d+([.]\d*)?([eE][+-]?\d+)?)|([.]\d+([eE][+-]?\d+)?)")

# bind operators to token types
ex_operators = {
    ";": TOKEN_SEMICOLON,
    "(": TOKEN_LPAREN,
    ")": TOKEN_RPAREN,
    ",": TOKEN_COMMA,
    "$": TOKEN_DOLLAR,
    "..": TOKEN_POINTPOINT,
    "=e=": TOKEN_EQNTYPE,
    "=l=": TOKEN_EQNTYPE,
    "=g=": TOKEN_EQNTYPE,
    "=E=": TOKEN_EQNTYPE,
    "=L=": TOKEN_EQNTYPE,
    "=G=": TOKEN_EQNTYPE,
}

un_op_names = ["+", "-", "not"]

operator_priority = {
    "+": 3,
    "-": 3,
    "/": 2,
    "*": 2,
    "**": 1,
    "=": 4,
    "<>": 4,
    ">": 4,
    ">=": 4,
    "<": 4,
    "<=": 4,
    "not": 5,
    "and": 6,
    "or": 7,
    "xor": 7,
}

operator_names = list(set(list(operator_priority) + un_op_names))

all_operators = dict()
for name in operator_names:
    all_operators[name] = TOKEN_OPERATOR

operators = {**all_operators, **ex_operators}

operator_re = re.compile(
    f"({'|'.join(re.escape(x) for x in sorted(operators, key=lambda x: -len(x)))})"
)


class Scaner(BaseScaner):
    def __init__(self, text: str):
        def default_action(pos: Position, token: str, value: str) -> (Token, Position):
            return Token(pos, token, value), Position(pos.source,
                                                      pos.line,
                                                      pos.pos + len(value),
                                                      pos.offset + len(value))

        super(Scaner, self).__init__(text, [
            ScanerRule(white_space_re, TOKEN_WHITE_SPACE, default_action),
            ScanerRule(new_line_re, TOKEN_NEW_LINE,
                       lambda pos, token, value: (Token(pos, token, value),
                                                  Position(self._text_by_line[pos.line],
                                                           pos.line + 1,
                                                           0,
                                                           pos.offset + len(value)))),
            ScanerRule(comment_re, TOKEN_COMMENT,
                       lambda pos, token, value: (Token(pos, token, value[1:]),
                                                  Position(pos.source,
                                                           pos.line,
                                                           pos.pos + len(value),
                                                           pos.offset + len(value)))),
            ScanerRule(label_re, TOKEN_LABEL,
                       lambda pos, token, value: (Token(pos, token, value[1:-1]),
                                                  Position(pos.source,
                                                           pos.line,
                                                           pos.pos + len(value) - 1,
                                                           pos.offset + len(value) - 1))
                       if value[-1] != "'" else (Token(pos, token, value[1:-1]),
                                                 Position(pos.source,
                                                          pos.line,
                                                          pos.pos + len(value),
                                                          pos.offset + len(value)))
                       ),
            ScanerRule(number_re, TOKEN_NUMBER, default_action),
            ScanerRule(operator_re, TOKEN_OPERATOR,
                       lambda pos, token, value: (Token(pos, operators[value], value),
                                                  Position(pos.source,
                                                           pos.line,
                                                           pos.pos + len(value),
                                                           pos.offset + len(value)))),
            ScanerRule(ident_re, TOKEN_IDENT, default_action),
        ])

        self.token = None

    def scan(self) -> Union[Token, None]:
        self.token = super().scan()
        if self.token is None:
            self.token = Token(self.pos, TOKEN_END, '\0')
        return self.token
