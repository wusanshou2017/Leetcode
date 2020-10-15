from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l =0
        r= len(nums)-1
        
        while l<r:
            mid =(l+r)//2
            # 旋转点 在左区间
            if nums[mid]<nums[r]:
                r=mid
                
            #旋转点 在右区间
            else: 
                l=mid+1
                
        return nums[l]

test =[5,6,7,0,1]
so =Solution()
print(so.findMin(test))