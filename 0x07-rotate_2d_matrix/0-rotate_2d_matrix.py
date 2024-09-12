#!/usr/bin/python3

"""
Defining a function that rotates a given 
n x n 2D matrix by 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Defininng the rotate_2d_matrix function
    Args:
        matrix(list of lists): A 2D matrix 
    """
    n = len(matrix)

    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
    for i in range(n):
        matrix[i].reverse()