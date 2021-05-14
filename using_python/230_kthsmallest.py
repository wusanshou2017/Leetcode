# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def preOrder(r: TreeNode):
            if not r:
                return []
            return [r.val] + preOrder(r.left) + preOrder(r.right)
        res_lst = preOrder(root)
        res_lst.sort(reverse=True)
        return res_lst[-k]
