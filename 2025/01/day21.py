# Leetle Day 21 - Factorial
# 21.01.2025

def solve(n):
    factorial = 1
    if n == 0:
        return factorial
    for i in range(1, n + 1):
        factorial *= i
    return factorial