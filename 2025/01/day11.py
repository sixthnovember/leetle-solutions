# Leetle Day 11 - Palindrome Check
# 11.01.2025

def solve(s):
    s_alnum = ""
    for i in s:
        if i.isalnum():
            s_alnum += i.lower()
    if s_alnum == s_alnum[::-1]:
        return True
    else:
        return False