# Leetle Day 19 - Binary Tree Maximum Depth
# 19.01.2025

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root):
    if not root:
        return 0
    left_depth = solve(root.left)
    right_depth = solve(root.right)
    return max(left_depth, right_depth) + 1