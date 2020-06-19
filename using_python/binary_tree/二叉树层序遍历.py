# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """docstring for  Solution """

    def levelOrder(self, root: TreeNode) -> [[int]]:

        if not root:
            return []
        from collections import deque

        layer = deque()
        layer.append(root)
        res = []
        while layer:
            cur_layer = []
            for _ in range(len(layer)):
                node = layer.popleft()
                cur_layer.append(node.val)
                if node.left:
                    layer.append(node.left)
                if node.right:
                    layer.append(node.right)
            res.append(cur_layer)
        return res


l = [9, 88, 88, 14, 25]
max_list = max(l)  # 返回最大值
max_index = l.index(max(l))  # 最大值的索引

print(max_list)
print(max_index)
print(l)
