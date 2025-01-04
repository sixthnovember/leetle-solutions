# Leetle Day 2 - Single Number
# 02.01.2025

def solve(nums):
    for i in nums:
        counter = 0
        for j in nums:
            if i == j:
                counter += 1
        if counter == 1:
            return i