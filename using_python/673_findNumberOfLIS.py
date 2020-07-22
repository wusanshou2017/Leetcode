# 输入: [1,3,5,4,7]
# 输出: 2
# 输入: [2,2,2,2,2]
# 输出: 5

class Solution:
    def findRotateNum(self, nums: [int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < nums[r]:

    def findNumberOfLIS(self, nums: [int]) -> int:
        pass
        return
