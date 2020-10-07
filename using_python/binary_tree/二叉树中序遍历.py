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

        if root is None:
            return []

        stack, output = [root.left, ], []
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)

                if root.left is not None:
                    stack.append(root.left)
        return output
