_program_list = {}


def register_program(name, klass):
    _program_list[name]= klass


def get(name):
    if name in _program_list:
        return _program_list[name]
    else:
        return None


import programs.exit
import programs.scan
import programs.proclist