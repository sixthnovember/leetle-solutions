# Leetle Day 8 - Two Sum
# 08.01.2025

def solve(nums, target):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []