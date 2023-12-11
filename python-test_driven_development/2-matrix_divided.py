#!/usr/bin/python3
"""Module to divide a matrix by number"""


def matrix_divided(matrix, div):
    """Function to divide a matrix
        args:
            matrix(list of lists_
            div(float or int)"""
    if type(matrix) != list:
        raise TypeError("""matrix must be a matrix 
                (list of lists) of integers/floats""")
    if any([type(i) != list for i in matrix]):
        raise TypeError("""matrix must be a matrix "
                "(list of lists) of integers/floats""")
    if any(type(j) not in [int, float] for i in matrix for j in i):
        raise TypeError("matrix must be a matrix "
                "(list of lists) of integers/floats")
    if not all(len(i) == len(matrix[0]) for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(ele/div, 2) for ele in row] for row in matrix]
