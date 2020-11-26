#  [1,8,6,2,5,4,8,3,7]
#  49

class Solution:
    def solve_most(self, nums: [int]) -> int:
        left, right = 0, len(nums) - 1
        ans = 0

        while left < right:
            if nums[left] > nums[right]:
                ans = max((right - left) * nums[right], ans)
                right -= 1

            else:
                ans = max((right - left) * nums[left], ans)
                left += 1



        return ans


so = Solution()

print(so.solve_most([1,1,1,1]))
