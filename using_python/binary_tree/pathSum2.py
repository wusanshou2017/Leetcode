# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        res = []
        path = []

        def dfs(res, path, node, target):
            if not node:
                return

            path.append(node.val)
            if not node.left and not node.right and target - node.val == 0:
                res.append(path[:])
            dfs(res, path, node.left, target - node.val)
            dfs(res, path, node.right, target - node.val)
            path.pop()

        dfs(res, path, root, sum)
        return res
