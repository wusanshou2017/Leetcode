class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0

    def divide(self, N: int) -> bool:

        dp = [False]
        for i in range(2, N + 1):
            dp[i] = any(not dp[i - j - 1]
                        for j in range(1, (i // 2) + 1) if i % j == 0)
        print(dp)
        return dp[-1]


so = Solution()

print(so.divide(4))
