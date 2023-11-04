#!/usr/bin/python3
def number_keys(a_dictionary):
    x = sorted(a_dictionary.keys())
    for i in x:
        print(f'{i}: {a_dictionary[i]}')
