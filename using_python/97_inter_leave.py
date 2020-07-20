class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(m + 1):
            for j in range(n + 1):
                if i == 0 and j == 0:
                    continue
                if i == 0 and j > 0:
                    if s3[j - 1] == s2[j - 1]:
                        dp[i][j] == dp[i][j - 1]
                if i > 0 and j == 0:
                    if s3[i - 1] == s1[i - 1]:
                        dp[i][j] == dp[i - 1][j]
                if i > 0 and j > 0:
                    if (s3[i - 1 + j - 1] == s1[i - 1]) or (s3[i - 1 + j - 1] == s2[j - 1]):
                        dp[i][j] = dp[i - 1][j] or dp[i][j - 1]

        print(dp)
        return dp[m][n]


so = Solution()
print(so.isInterleave("123", "456", "145623"))
