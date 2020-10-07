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

        return self.Traversal(root.left)  + self.Traversal(root.right)+[root.val]

    def Traversal2(self, root: TreeNode) -> List[int]:
        res =[]
        stack =[]
        cur =root 
        while stack or cur:
            while  cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            cur = cur.left
        return res[::-1]
