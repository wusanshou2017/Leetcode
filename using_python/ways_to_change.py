class Solution:
    def waysToChange(self, n: int) -> int:
        mod = 10**9 + 7
        coins = [25, 10, 5, 1]
        dp = [1] + n * [0]

        for coin in coins:
            for i in range(coin, n + 1):
                dp[i] += dp[i - coin]

        return dp[n]


so = Solution()
print(so.waysToChange(65465))
