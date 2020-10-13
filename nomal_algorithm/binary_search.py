from typing import List
# this solution for test binary search is ruboost or not
import random


class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r-l) // 2
            if target > nums[mid]:
                l = mid +1
            elif target == nums[mid]:
                return mid
            else:
                r = mid-1

        return -1


# generate some test_demo  such as nums and targets to test the bianary search
# dead loop or not
nums = [random.randint(0, 1000) for i in range(2000)]
nums.sort()


so = Solution()
for i in range(1000):
    print("index...:", i)
    print("res:...", so.binarySearch(nums, i))
