# Leetle Day 13 - Running Sum
# 13.01.2025

def solve(nums):
    running_sum = []
    current_sum = 0
    for i in nums:
        current_sum += i
        running_sum.append(current_sum)
    return running_sum