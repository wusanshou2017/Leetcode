class Solution:
    # 
    # def isOneEditDistance(self, s: str, t: str) -> bool:
    #     m = len(s)
    #     n = len(t)
    #     if m - n > 1 or n - m > 1:
    #         return False

    #     dp = [[i + j for i in range(n + 1)]for j in range(m + 1)]

    #     for i in range(1, m + 1):
    #         for j in range(1, n + 1):
    #             if s[i - 1] == t[j - 1]:
    #                 d = 0
    #             else:
    #                 d = 1
    #             dp[i][j] = min(dp[i - 1][j] + 1, dp[i]
    #                            [j - 1] + 1, dp[i - 1][j - 1] + d)

    #     return dp[m][n] == 1

    def isOneEditDistance(self, s: str, t: str) -> bool:
        m = len(s)
        n = len(t)

        if m> n:
            return self.isOneEditDistance(t, s)
        
        if n-m>1:
            return False 
        
        for i in range(m):
            if s[i]!= t[i]:
                if m==n:
                    return s[i+1:]==t[i+1:]
                
                else:
                    return s[i:]==t[i+1:]
        
        return m+1 == n

# "ab"
# "acb"
so = Solution()
print(so.isOneEditDistance("abc", "acb"))
