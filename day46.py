# Leetle Day 46 - Container With Most Water
# 15.02.2025

def solve(height):
    left = 0
    right = len(height) - 1
    max_water = 0
    while left < right:
        width = right - left
        min_height = min(height[left], height[right])
        max_water = max(max_water, min_height * width)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_water