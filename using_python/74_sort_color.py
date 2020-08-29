from typing import List 
# 输入: [2,0,2,1,1,0]
# 输出: [0,0,1,1,2,2]
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0,curr,p2 = 0,0,len(nums)-1
        while curr<=p2:
        	if nums[curr]==0:
        		nums[p0],nums[curr] =nums[curr],nums[p0]
        		p0+=1
        	elif nums[curr]==2:
        		nums[curr],nums[p2] = nums[p2],nums[p0]
        	else:
        		curr+=1
