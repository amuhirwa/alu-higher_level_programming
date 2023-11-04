#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    best = max(a_dictionary.values())
    for i in a_dictionary:
        if a_dictionary[i] == best:
            return i
