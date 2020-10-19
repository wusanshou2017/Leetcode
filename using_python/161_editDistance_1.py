class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
    	m = len(s)
    	n = len(t)
    	dp=[ [i+j for i in range(n+1) ]for j in range (m+1)]
    	print(dp)
    	for i in range (1,m+1):
    		for j in range(1,n+1):
    			if s[i-1] ==t[j-1]:
    				d =0
    			else:
    				d=1
    			dp[i][j] = min (dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+d)
    	print(dp)

    	return dp[m-1][n-1]==1

# "ab"
# "acb"
so =Solution()
print (so.isOneEditDistance("a",""))