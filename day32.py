# Leetle Day 32 - Find First and Last Position of Element in Sorted Array
# 01.02.2025

def solve(nums, target):
    indices = []
    for i in range(len(nums)):
        if nums[i] == target:
            indices.append(i)
    if len(indices) == 0:
        indices = [-1,-1]
    if len(indices) == 1:
        indices.append(indices[0])
    return indices