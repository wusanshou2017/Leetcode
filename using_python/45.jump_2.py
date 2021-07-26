# 输入: [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
#      从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        fathest = 0
        end = 0
        jumps = 0
        for i in range(len(nums) - 1):
            # 此处做贪心 找最远距离
            fathest = max(fathest, nums[i] + i)
            if i == end:
                jumps += 1
                end = fathest
        return jumps