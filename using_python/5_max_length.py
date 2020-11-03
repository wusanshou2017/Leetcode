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
<<<<<<< HEAD
        dp = [[False] * n for _ in range(n)]
        for i in range (n):
            dp[i][i] =True
        for i in range (n):
            for j in range ():
                dp[i][j] = (s[i]==s[j] and dp[i-1][j-1]):
                if dp[]


=======
        if n < 2:
            return s
        res = ""
        for i in range(1, n):
            move=0
            
            while i-1-move>=0 and i+move+1<=n and self.check(s[i-1-move:i+move+1]):
                if 2+2*move>len(res):
                    res =s[i-1-move:i+move+1]
                move+=1
           
            move =0
            while i-move>=0 and i+move+1<=n and self.check(s[i-move:i+move+1]):
                if 1+2*move>len(res):
                    res =s[i-move:i+move+1]
                move+=1

        return res
>>>>>>> 1b7336656903a86992c98cd33368f2f2b0740d31

    def longestPalindrome2(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        dp = [[False]*n for _ in range(n)]
        for i in range(n):
            dp[i][i]=True

        res_len=0
        res =s[0]
        for j in range(1,n):
            for i in range(0,j):
                if j-i<3 and s[i]==s[j]:
                    dp[i][j]=True
                else:
                    dp[i][j] = dp[i+1][j-1] and s[i]==s[j]
                if dp[i][j]:
                    if j-i+1>res_len:
                        res_len =j-i+1
                        res =s[i:j+1]
        
        return res
    def check(self, s: str):
        return s[:] == s[::-1]


so = Solution()
<<<<<<< HEAD
print(so.longestPalindrome("cbbd"))
=======
print(so.longestPalindrome2("cbbd"))
>>>>>>> 1b7336656903a86992c98cd33368f2f2b0740d31
