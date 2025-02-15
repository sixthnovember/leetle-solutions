# Leetle Day 38 - Balanced Binary Tree
# 07.02.2025

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_balance(node):
    if not node:
        return 0, True
    left_height, is_left_balanced = check_balance(node.left)
    right_height, is_right_balanced = check_balance(node.right)
    if not is_left_balanced or not is_right_balanced:
        return 0, False
    height_difference = abs(left_height - right_height)
    if height_difference > 1:
        return 0, False
    current_height = max(left_height, right_height) + 1
    return current_height, True

def solve(root):
    height, is_balanced = check_balance(root)
    return is_balanced