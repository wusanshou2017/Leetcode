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
        if n < 2:
            return s
        res = ""
        for i in range(n):
            left, right = 0, 0
            while i - left >= 0 and i + right <= n - 1:
                if self.check(s[i - left:i + right + 1]):
                    if len(s[i - left:i + right + 1]) > len(res):
                        res = s[i - left:i + right + 1]
                elif self.check(s[i - left:i + right + 2]):
                    if len(s[i - left:i + right + 2]) > len(res):
                        res = s[i - left:i + right + 2]
                left += 1
                right += 1

        return res if res != "" else s[0]

    def check(self, s: str):
        return s[:] == s[::-1]


so = Solution()
print(so.longestPalindrome("cbbd"))
