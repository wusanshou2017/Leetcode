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

        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]

        if len(neg_lst) >= 2:
            if len(pos_lst) > 2:
                return max(neg_lst[0] * neg_lst[1] * pos_lst[-1], pos_lst[-2] * pos_lst[-1] * pos_lst[-3])

            return neg_lst[0] * neg_lst[1] * pos_lst[-1]

        else:
            if len(pos_lst) < 3:
                return 0
            else:
                return pos_lst[-2] * pos_lst[-1] * pos_lst[-3]


so = Solution()

print(so.maximumProduct([-100, -98, -1, 2, 3, 4]))
