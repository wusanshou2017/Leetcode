# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def reverse(self,root:TreeNode)->TreeNode:
        if not root:
            return []
        root.left,root.right = root.right,root.left
        self.reverse(root.left)
        self.reverse(root.right)
        return root