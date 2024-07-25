#!/usr/bin/python3

"""This defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """
    This represents Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    Returns an empty list if n <= 0
    Args:
        n: number of rows
    """
    if n <= 0:
        return [] #return empty list

    triangle = [[1]] #list of lists
    while len(triangle) != n:
        trn = triangle[-1] #last list in the triangle
        tmpy = [1] #first element of every list
        for i in range(len(trn) - 1):
            tmpy.append(trn[i] + trn[i + 1]) 
        tmpy.append(1) #last element of every list
        triangle.append(tmpy) #add latest list
    return triangle