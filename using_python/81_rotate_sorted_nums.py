# input:nums = [2,5,6,0,0,1,2], target = 0
# output:True
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
        	return False
        l = 0
        r = len(nums)-1

        while l<=r:
        	mid =(l+r)//2
        	if nums[mid] == target:
        		return True

        	## left range
        	if nums[mid]>nums[l]:
        		if nums[l]<=target<=nums[mid]:
        			r =mid-1

        		else:
        			l =mid +1

        	elif nums[mid] == nums[l]:
        		l +=1

        	### right range
        	elif nums[mid]<nums[l]:
        		if nums[mid]<= target <= nums[r]:
        			l = mid +1
        		else:
        			r =mid -1

        return False 
