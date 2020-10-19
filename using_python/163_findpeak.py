class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        r =len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid-1]<nums[mid] and nums[mid]> nums[mid+1]:
                return mid
            else:
                if nums[mid]>nums[r]:
                    r = mid
                
                elif nums[mid]<nums[l]:
                    l= mid+1
        return -1

