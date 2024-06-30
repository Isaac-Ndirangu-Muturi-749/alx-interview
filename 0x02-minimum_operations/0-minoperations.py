#!/usr/bin/python3
"""
Module 0-minoperations
"""


def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    divisor = 2  # smallest prime number

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor

        divisor += 1

    return operations
