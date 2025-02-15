# Leetle Day 6 - Maximum Subarray
# 06.01.2025

def solve(nums):
    maxSum = float('-inf')
    currentSum = 0
    for i in nums:
        currentSum += i
        if currentSum > maxSum:
            maxSum = currentSum
        if currentSum < 0:
            currentSum = 0
    return maxSum