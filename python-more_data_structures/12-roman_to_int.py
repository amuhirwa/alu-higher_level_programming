#!/usr/bin/python3
def roman_to_int(strs):
    rom_nums = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    sum = 0
    minus = 0
    for i in range(len(strs)):
        if i != len(strs) - 1:
            if rom_nums[strs[i]] < rom_nums[strs[i+1]]:
                minus = -(rom_nums[strs[i]])
            else:
                sum += minus + rom_nums[strs[i]]
                minus = 0
        else:
            sum += minus + rom_nums[strs[i]]
    return sum
