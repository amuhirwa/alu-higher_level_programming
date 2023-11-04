#!/usr/bin/python3
def no_c(my_string):
    list_string = list(my_string)
    list_string = [i for i in list_string if i.lower() != 'c']
    return ''.join(list_string)
