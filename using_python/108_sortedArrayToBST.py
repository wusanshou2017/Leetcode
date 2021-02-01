# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
#
#         给定有序数组: [-10,-3,0,5,9],

# 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：


#       0
#      / \
#    -3   9
#    /   /
#  -10  5
from typing import List


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.helper(0, len(nums) - 1, nums)

    def helper(self, left: int, right: int, nums: List[int]):
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        print("mid:...", mid)
        root.left = self.helper(left, mid - 1, nums)
        root.right = self.helper(mid + 1, right, nums)
        return root


data_test = [-10, -3, 0, 5, 9]
so = Solution()
print(so.sortedArrayToBST(data_test))
