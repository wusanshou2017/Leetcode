class Solution:
    def findMagicIndex(self, nums: [int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if mid < nums[mid]:
                r = mid - 1

            elif mid > nums[mid]:
                l = mid + 1

            else:
                return mid

        return -1


so = Solution()

nums = [0, 0, 3]

print(so.findMagicIndex(nums))
