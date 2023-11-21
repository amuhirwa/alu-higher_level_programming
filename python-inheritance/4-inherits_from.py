#!/usr/bin/python3

def inherits_from(obj, a_class):
    if type(obj).__base__ == a_class:
        return True
    return False
