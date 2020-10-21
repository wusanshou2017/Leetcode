class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)
        if m - n > 1 or n - m > 1:
            return False

        dp = [[i + j for i in range(n + 1)]for j in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    d = 0
                else:
                    d = 1
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i]
                               [j - 1] + 1, dp[i - 1][j - 1] + d)

        return dp[m][n] == 1


# "ab"
# "acb"
so = Solution()
print(so.isOneEditDistance("abc", "acb"))
