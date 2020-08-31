# 给定 nums = [1,1,1,2,2,3],

# 函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
    	p0,p1 =1,1
    	n = len(nums)
    	for i in range(1,n):
    		if nums[i]==nums[i-1]:
    			p1+=1
    		else:
    			p1=1
    		if p1<=2:
    			nums[p0]=nums[i]
    			p0+=1
    	print(nums)
    	return p0 

nums = [1,1,1,1,2,2,2,3]

so =Solution()
print(so.removeDuplicates(nums))
