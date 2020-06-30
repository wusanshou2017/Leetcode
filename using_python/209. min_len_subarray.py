# 输入：s = 7, nums = [2,3,1,2,4,3]
# 输出：2

class Solution:
    def minSubArrayLen(self, s: int, nums: [int]) -> int:
        n = len(nums)
        slow_ptr = 0
        fast_ptr = 0
        ans = float("inf")
        total = 0
        while fast_ptr < n:
            total += nums[fast_ptr]
            while total >= s:
                ans = min(ans, fast_ptr - slow_ptr + 1)
                total -= nums[slow_ptr]
                slow_ptr += 1
            fast_ptr += 1

        return ans if ans != float("inf") else 0


so = Solution()

print(so.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
