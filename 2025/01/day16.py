# Leetle Day 16 - Longest Consecutive Sequence
# 16.01.2025

def solve(nums):
    if len(nums) == 0:
        return 0
    nums.sort()
    counter = 1
    max_counter = 1
    for i in range(len(nums)-1):
        if nums[i + 1] == nums[i] + 1:
            counter += 1
            if counter > max_counter:
                max_counter = counter
        elif nums[i + 1] != nums[i]:
            counter = 1
    return max_counter