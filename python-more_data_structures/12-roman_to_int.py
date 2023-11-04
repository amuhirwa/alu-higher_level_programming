#!/usr/bin/python3
def roman_to_int(strs):
    if type(strs) is not str:
        return 0
    roms = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    sum = 0
    minus = 0
    for i in range(len(strs)):
        if i != len(strs) - 1:
            if roms[strs[i]] < roms[strs[i+1]]:
                minus = -(roms[strs[i]])
            else:
                sum += minus + roms[strs[i]]
                minus = 0
        else:
            sum += minus + roms[strs[i]]
    return sum
