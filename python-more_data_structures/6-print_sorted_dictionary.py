#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    x = sorted(a_dictionary.keys())
    for i in x:
        print(f'{i}: {a_dictionary[i]}')
