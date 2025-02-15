# Leetle Day 41 - 3Sum Closest
# 10.02.2025

def solve(nums, target):
    closest_sum = float('inf')
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                current_sum = nums[i] + nums[j] + nums[k]
                diff_closest = closest_sum - target
                diff_current = current_sum - target
                if diff_current < 0:
                    diff_current = -diff_current
                if diff_closest < 0:
                    diff_closest = -diff_closest
                if diff_current < diff_closest:
                    closest_sum = current_sum
    return closest_sum