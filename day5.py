# Leetle Day 5 - Valid Anagram
# 05.01.2025

def solve(s1, s2):
    if sorted(s1) == sorted(s2):
        return True
    return False