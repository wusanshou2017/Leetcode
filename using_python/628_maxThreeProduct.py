# [-100,-98,-1,2,3,4]
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        neg_lst = []
        pos_lst = []
        for num in nums:
            if num < 0:
                neg_lst.append(num)

            else:
                pos_lst.append(num)

        return max(nums[0]*nums[1]*nums[-1], nums[-3]*nums[-2]*nums[-1]) 


so = Solution()

print(so.maximumProduct([-100, -98, -1, 2, 3, 4]))
