# Leetle Day 34 - Binary Tree Inorder Traversal
# 03.02.2025

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def solve(root):
    if not root:
        return []
    return solve(root.left) + [root.val] + solve(root.right)