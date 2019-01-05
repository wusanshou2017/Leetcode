class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target > max(nums):
            return len(nums)
        if target < min(nums):
            return 0
        i = 0
        j = len(nums) - 1
        while i < j - 1:
            mid = (i+j)/2
            if nums[mid] < target:
                i = mid
            elif nums[mid] > target:
                j = mid
            else:
                return mid
        if nums[i] == target:
            return i
        return j