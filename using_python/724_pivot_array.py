# test_data =[1, 7, 3, 6, 5, 6]
# test_data = [-1,-1,-1,0,1,1]
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # define the mid index which the left sum is equal to right sum
        if len(nums) < 3:
            return -1

        n = len(nums)
        index_sum_dict = {}
        index_sum_dict[0] = 0
        index_sum_dict[1] = nums[0]
        # to compute all index sum of left
        for i in range(2, n):
            index_sum_dict[i] = index_sum_dict[i - 1] + nums[i - 1]

        total = index_sum_dict[n - 1] + nums[n - 1]
        for i in range(0, n):
            if total - index_sum_dict[i] - nums[i] == index_sum_dict[i]:
                return i

        else:
            return -1


so = Solution()
print(so.pivotIndex([-1, -1, -1, 0, 1, 1]))
