#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    if type(obj) == a_class:
        return True
    if type(obj).__base__ == a_class:
        return True
    return False
