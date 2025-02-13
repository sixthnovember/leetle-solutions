# Leetle Day 44 - Longest Palindromic Substring
# 13.02.2025

def solve(s):
    if not s:
        return ""
    longest = s[0]
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if substring == substring[::-1] and len(substring) > len(longest):
                longest = substring
    return longest