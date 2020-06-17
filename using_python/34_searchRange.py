class Solution():
    def extreme_index(self,nums:[int],target,left):
        low= 0
        high= len(nums)
        while low<high:
            mid =(low +high)//2
            if nums[mid]>target or  (left and nums[mid]==target):
                high =mid
            else:
                low =mid+1

        return low


    def searchRange(self,nums:[int],target)->[int]:
        low = self.extreme_index(nums,target,True)
        if low == len(nums) or nums[low] != target:
            return [-1, -1]
        high =self.extreme_index(nums,target,False)-1
        if high<low:
            high=low
        return [low ,high]

l=[1,2,2,5,5,5,7,8,9]

so =Solution()
print (so.searchRange(l,5))
