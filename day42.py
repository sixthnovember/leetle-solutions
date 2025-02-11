# Leetle Day 42 - Longest Substring Without Repeating Characters
# 11.02.2025

def solve(s):
    max_length = 0
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_length = max(max_length, j - i + 1)
    return max_length