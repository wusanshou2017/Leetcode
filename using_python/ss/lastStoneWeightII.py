class Solution:
    def lastStoneWeightII(self, stones: [int]) -> int:

        sums = sum(stones)
        half = sums // 2

        dp = [0] * (half + 1)

        for stone in stones:
            for j in range(len(dp) - 1, stone - 1, -1):
                dp[j] = max(dp[j], dp[j - stone] + stone)

        return sums - 2 * dp[half]


so=Solution()
test =[2,7,4,1,8,1]
print (so.lastStoneWeightII(test))
