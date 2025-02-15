# Leetle Day 27 - Power of Two
# 27.01.2025

def solve(n):
    power = 1
    for i in range(n):
        if power == n:
            return True
        power *= 2
    return False