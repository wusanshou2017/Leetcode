# input:nums = [2,5,6,0,0,1,2], target = 0
# output:True
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            mid = l + (r - l) // 2
            # left
            if nums[0] < nums[mid]:
