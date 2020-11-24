class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m =len(p)
        n = len(s)
        dp = [ [False] * (n+1) for _ in range(m+1) ]
        dp[0][0]=True
        for i in range(1,m+1):
            for j in range(0,n+1):
                if p[i-1]=="*":
                    dp[i][j] |=dp[i-2][j]
                    if (p[i-2]=="." and j>0) or (p[i-2]==s[j-1]):
                        dp[i][j] |= dp[i][j-1]
                else:
                    dp[i][j] = i>0 and ((p[i-1]==s[j-1])or p[i-1]==".") and dp[i-1][j-1]
        
        return dp[m][n]

so =Solution()
print(so.isMatch("aa","a*"))