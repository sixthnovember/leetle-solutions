# Leetle Day 7 - Valid Parentheses
# 07.01.2025

def solve(s):
    stack = []
    dict = {')': '(', '}': '{', ']': '['}
    for c in s:
        if c in dict.values():
            stack.append(c)
        elif c in dict.keys():
            if len(stack) == 0:
                return False
            if dict[c] != stack[-1]:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False