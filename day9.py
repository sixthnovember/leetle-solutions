# Leetle Day 9 - Sliding Window Maximum
# 09.01.2025

from collections import deque

def solve(nums, k):
    if not nums or k == 0:
        return []
    deq = deque()
    result = []
    for i in range(len(nums)):
        if len(deq) > 0 and deq[0] < i - k + 1:
            deq.popleft()
        while len(deq) > 0 and nums[deq[-1]] < nums[i]:
            deq.pop()
        deq.append(i)
        if i >= k - 1:
            result.append(nums[deq[0]])
    return result