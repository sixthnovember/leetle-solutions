# Leetle Day 3 - Majority Element
# 03.01.2025

def solve(nums):
    max_element = len(nums) // 2
    for i in nums:
        counter = 0
        for j in nums:
            if i == j:
                counter += 1
        if counter > max_element:
            return i