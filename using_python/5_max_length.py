class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     n = len(s)
    #     if n < 2:
    #         return s
    #     res = ""
    #     for j in range(0, n + 1):
    #         for i in range(j):

    #             if s[i:j] == s[j:i:-1]:
    #                 if j - i > len(res):
    #                     res = s[i:j]
    #     return res

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range (n):
            dp[i][i] =True
        for i in range (n):
            for j in range ():
                dp[i][j] = (s[i]==s[j] and dp[i-1][j-1]):
                if dp[]



    def check(self, s: str):
        return s[:] == s[::-1]


so = Solution()
print(so.longestPalindrome("cbbd"))
