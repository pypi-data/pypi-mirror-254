#  --------------------------------------------------------------------------------
#  Izok: A modeling system similar to GAMS for pyomo.
#  Copyright 2024,  Andrey Sergeevich Storozhenko, All rights reserved.
#  This software is distributed under the 3-clause BSD License.
#  --------------------------------------------------------------------------------

from typing import Tuple, Pattern, Callable, NamedTuple, List, Union
from .position import Position
from .token import Token


class ScanerRule(NamedTuple):
    pattern: Pattern[str]
    token: str
    action: Callable[[Position, str, str], Tuple[Token, Position]]


class BaseScaner:
    def __init__(self, text: str, rules: List[ScanerRule]):
        self.text = text
        self._text_by_line = (text+'\n').splitlines()
        self.pos = Position(self._text_by_line[0], 1, 0, 0)
        self._rules = rules

    def scan(self) -> Union[Token, None]:
        if self.pos.offset >= len(self.text):
            return None

        matches = []

        for r in self._rules:
            m = r.pattern.match(self.text, self.pos.offset)

            if m is None:
                continue

            value = m.group()

            if value == '':
                continue

            matches.append((r, m.group()))

        if len(matches) != 0:
            matches.sort(key=lambda x: -len(x[1]))
            rule, value = matches[0]
            token, self.pos = rule.action(self.pos, rule.token, value)
            return token

        token = Token(self.pos, "", self.text[self.pos.offset])
        self.pos.pos += 1
        self.pos.offset += 1
        return token
