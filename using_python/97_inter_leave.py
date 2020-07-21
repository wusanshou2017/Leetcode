class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(1, m + 1):
            dp[i][0] = (dp[i - 1][0] and s1[i - 1] == s3[i - 1])
        for i in range(1, n + 1):
            dp[0][i] = (dp[0][i - 1] and s2[i - 1] == s3[i - 1])

        for i in range(1, m + 1):
            for j in range(1, n + 1):

                dp[i][j] = (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                            ) or (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])

        return dp[m][n]


so = Solution()
print(so.isInterleave("ab", "bc", "bbac"))
