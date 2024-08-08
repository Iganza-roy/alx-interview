#!usr/bin/env python3

"""
Creating a function that calculates the fewest number of operations
needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Defining the minOperations function to do the calculations
    Args: 
        n (int): The number of H characters in the file
    """
    if n < 2:
        return 0
    
    operations = 0
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1
    
    return operations
