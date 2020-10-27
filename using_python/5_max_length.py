class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        res = ""
        for j in range(0, n + 1):
            for i in range(j):

                if self.check(s[i:j]):
                    if j - i > len(res):
                        res = s[i:j]
        return res

    def check(self, s: str):
        return s[:] == s[::-1]


so = Solution()
print(so.longestPalindrome(""))
