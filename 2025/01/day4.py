# Leetle Day 4 - Missing Number
# 04.01.2025

def solve(nums):
    total_sum = 0
    actual_sum = 0
    for i in range(len(nums) + 1):
        total_sum += i
    for num in nums:
        actual_sum += num
    return total_sum - actual_sum