# Leetle Day 25 - Climbing Stairs
# 25.01.2025

def solve(n):
    if n == 0 or n == 1 or n == 2:
        return n
    prev2 = 1
    prev1 = 2
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    return prev1