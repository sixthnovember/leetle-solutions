# Leetle Day 33 - Number of Steps to Reduce to Zero
# 02.02.2025

def solve(num):
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
        steps += 1
    return steps