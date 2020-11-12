# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        self.ans=1
        def dfs(root):
            if not root:
                return 0
            
            l = dfs(root.left)
            r =dfs (root.right)

            self.ans = max(l+r+1,self.ans)
            return max(l,r)+1
        dfs(root)
        
        return self.ans-1