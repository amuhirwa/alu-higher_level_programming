#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    list_of_vals = list(map(lambda x: x * 2, a_dictionary.values()))
    x = list(a_dictionary.keys())
    a_dictionary = {x[i]: list_of_vals[i] for i in range(len(x))}
    return a_dictionary
