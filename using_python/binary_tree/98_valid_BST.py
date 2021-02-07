# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res = self.helper2(root)

        for i in range(1, len(res)):
            if res[i] <= res[i - 1]:
                return False
        else:
            return True

    def helper(self, root: TreeNode) -> []:
        if not root:
            return []
        return self.helper(root.left) + [root.val] + self.helper(root.right)

    def helper2(self, root: TreeNode) -> []:
        res = []
        stack = []
        cur = root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
