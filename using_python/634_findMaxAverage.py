from typing import List
# [1,12,-5,-6,50,3], k = 4
# output = 12.5


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) < k:
            return -1

        cur_sum = sum(nums[:k])

        cur_avg = cur_sum / k * 1.0
        for i in range(1, len(nums) - k + 1):

            cur_sum = cur_sum - nums[i - 1] + nums[i + k - 1]
            cur_avg = max(cur_sum / k * 1.0, cur_avg)

        return cur_avg


so = Solution()


print(so.findMaxAverage([1, 12, -5, -6, 50, 3], k=4))
