#  --------------------------------------------------------------------------------
#  Izok: A modeling system similar to GAMS for pyomo.
#  Copyright 2024,  Andrey Sergeevich Storozhenko, All rights reserved.
#  This software is distributed under the 3-clause BSD License.
#  --------------------------------------------------------------------------------

from .position import Position


class IzokException(Exception):
    def __init__(self, msg: str):
        super(IzokException, self).__init__(msg)


class Singleton:
    __instance = None

    def __init__(self):
        pass

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


class ExceptionConstructor(Singleton):
    def __init__(self):
        super(ExceptionConstructor, self).__init__()
        self.base_position = None
        self.scaner_source = ""

    def build_and_raise(self, current: Position, error_id: int, head_msg: str, tail_msg: str):
    
        if self.base_position is None:
            msg = "exception[E{:04d}]:{}".format(error_id, head_msg)
            msg += f"\n-->{self.scaner_source}:{current.line}:{current.pos}"
            num_count_in_line = len(f"{current.line}")
            line_number = f"\n{' ' * num_count_in_line}"
            msg += f"\n{current.line}|" + current.source
            msg += line_number + "|" + "-" * current.pos + "^"
            first = True
            for str_line in tail_msg.splitlines():
                if first:
                    msg += line_number + "=" + str_line
                    first = False
                else:
                    msg += line_number + " " + str_line
        else:
            msg = "exception[E{:04d}]:{}".format(error_id, head_msg)
            msg += f"\n-->{self.scaner_source}:{self.base_position.line}:{self.base_position.pos}"
            num_count_in_line = len(f"{current.line}")
            line_number = f"\n{' ' * num_count_in_line}"
            if self.base_position.line == current.line:
                msg += f"\n{self.base_position.line}|" + self.base_position.source
            else:
                msg += f"\n{self.base_position.line}|" + self.base_position.source
                if current.line - self.base_position.line > 1:
                    msg += line_number + "|" + '...'
                msg += f"\n{current.line}|" + self.base_position.source
            msg += line_number + "|" + "-" * current.pos + "^"
            first = True
            for str_line in tail_msg.splitlines():
                if first:
                    msg += line_number + "=" + str_line
                    first = False
                else:
                    msg += line_number + " " + str_line
    
        raise IzokException(msg)


def error(pos, error_id: int, head_msg: str, tail_msg: str):
    ExceptionConstructor().build_and_raise(pos, error_id, head_msg, tail_msg)


def set_base_position(value):
    ExceptionConstructor().base_position = value


def set_scaner_source(value):
    ExceptionConstructor().scaner_source = value
