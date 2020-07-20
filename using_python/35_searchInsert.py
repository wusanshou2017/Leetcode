
# 输入: [1,3,5,6], 5
# 输出: 2

# 输入: [1,3,5,6], 2
# 输出: 1

class Solution:
    def searchInsert(self, nums: [int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        if target > nums[r]:
            return n
        if target <= nums[l]:
            return 0
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            if nums[mid] < target:
                l = mid + 1
            if nums[mid] == target:
                return mid
        return l


so = Solution()

print(so.searchInsert([1, 3, 5, 6], 1))
