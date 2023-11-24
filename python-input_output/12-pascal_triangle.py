#!/usr/bin/python3
"""Module to output pascal's triangle"""


def pascal_triangle(n):
    """Function that returns pascal's triangle
        Args:
            n(int): number of rows in pascal's triangle
    """
    arr = []
    for i in range(n):
        new_arr = []
        for j in range(i+1):
            if j == 0 or j == i:
                new_arr.append(1)
            else:
                new_arr.append(arr[i-1][j]+arr[i-1][j-1])
        arr.append(new_arr)
    return arr
