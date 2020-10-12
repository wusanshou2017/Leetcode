# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue =collections.deque()
        layer =deque()
        layer.append(root)
        res =[]
        while layer:
            cur_layer =[]
            for _ in range(len(layer)):
                node = layer.popleft()
                cur_layer.append(node.val)
                if node.left:
                    layer.append(node.left)
                if node.right:
                    layer.append(node.right)
            res.append(cur_layer)
        return res[::-1]