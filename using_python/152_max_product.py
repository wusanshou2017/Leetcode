# 输入: [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6
from typing import List 

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    	ans =nums[0]
    	pre_min =nums[0]
    	pre_max =nums[0]
    	for i in range(1,len(nums)):
    		cur_min = min (pre_min*nums[i],pre_max*nums[i],nums[i])
    		cur_max = max(pre_min*nums[i],pre_max*nums[i],nums[i])
    		ans = max(ans,cur_max)
    		pre_max=cur_max
    		pre_min = cur_min
    	return ans


test =[2,3,0,-6,-2,4]
so =Solution()
print (so.maxProduct(test))
