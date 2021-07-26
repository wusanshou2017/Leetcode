from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Traversal(self, root: TreeNode) -> List[int]:
        # 递归解法
        if root is None:
            return []

        return self.Traversal(root.left) + [root.val] + self.Traversal(root.right)

    def Traversal2(self, root: TreeNode) -> List[int]:
        res =[]
        stack =[]
        cur =root 
        while stack or cur:
            while  cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append (cur.val)
            cur = cur.right
        return res

    def Traversal3 (self,root:TreeNode)->List[int]:
        res =[]
        stack =[]
        cur =root 

        

        



