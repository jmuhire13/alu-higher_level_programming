#!/usr/bin/python3


def pow(a, b):
    if b == 0:
        return 1  # Any number to the power of 0 is 1
    elif b < 0:
        result = 1
        for _ in range(abs(b)):
            result /= a  # Use division for negative powers
        return result
    else:
        result = 1
        for _ in range(b):
            result *= a  # Multiply for positive powers
        return result
