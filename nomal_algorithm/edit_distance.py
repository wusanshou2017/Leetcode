
class Solution():
    def editDistance(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        dp = [[i + j for i in range(n + 1)] for j in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # to_do
                if s1[i - 1] == s2[j - 1]:
                    d = 0

                else:
                    d = 1

                dp[i][j] = min(dp[i - 1][j - 1] + d, dp[i - 1]
                               [j] + 1, dp[i][j - 1] + 1)

        return dp[m - 1][n - 1]


so = Solution()

print(so.editDistance("a", ""))


