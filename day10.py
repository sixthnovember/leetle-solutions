# Leetle Day 10 - First Missing Positive
# 10.01.2025

def solve(nums):
    positive_nums = []
    for i in nums:
        if i > 0:
            positive_nums.append(i)
    positive_nums.sort()
    smallest_positive = 1
    for i in positive_nums:
        if i == smallest_positive:
            smallest_positive += 1
    return smallest_positive