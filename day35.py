# Leetle Day 35 - Counting Bits
# 04.02.2025

def solve(n):
    result = []
    for i in range(n + 1):
        count = 0
        num = i
        while num > 0:
            count += num & 1  # least significant bit
            num >>= 1  # right shift to next bit
        result.append(count)
    return result