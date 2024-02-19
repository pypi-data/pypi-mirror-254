#  --------------------------------------------------------------------------------
#  Izok: A modeling system similar to GAMS for pyomo.
#  Copyright 2024,  Andrey Sergeevich Storozhenko, All rights reserved.
#  This software is distributed under the 3-clause BSD License.
#  --------------------------------------------------------------------------------

class Box:
    def __init__(self, name: str, owner=None):
        self._owner = owner
        self._name = name
        self.value = None

    @property
    def name(self):
        return self._name

    @property
    def owner(self):
        return self._owner


class Domain:
    def __init__(self):
        self._domain = dict()

    def push_set(self, name: str, owner):
        self._domain[name] = [Box(name, owner)]

    def pop_set(self, name: str):
        self._domain[name].pop(-1)

    def get_set_by_name(self, name: str) -> Box:
        return self._domain[name][-1]

    def get_set_value(self, name: str):
        return self._domain[name][-1].value

    def set_set_value(self, name: str, value):
        self._domain[name][-1].value = value

    def __contains__(self, item: str):
        return item in self._domain
