# Leetle Day 28 - Reverse Integer
# 28.01.2025

def solve(n):
    INT_MIN = -2**31
    INT_MAX = 2**31 - 1
    if n < 0:
        reversed_str = "-" + str(n)[:0:-1]
    else:
        reversed_str = str(n)[::-1]
    reversed_int = int(reversed_str)
    if reversed_int < INT_MIN or reversed_int > INT_MAX:
        return 0
    return reversed_int