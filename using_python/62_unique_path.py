class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    	dp = [[1]*n]+[ [1]+[0]* (n-1) for _ in range (m-1)]
    	# print (dp)
    	# for i in range (n):
    	# 	dp[0][i]=1
    	# for j in range (m):
    	# 	dp[j][0]=1
    	for i in range (1,m):
    		for j in range (1,n):    			
    			dp[i][j] = dp[i-1][j]+dp[i][j-1]
    	return dp[-1][-1] 

    def test(self,m:int,n:int)->int :
    	pre_up=1
    	pre_left=1 
    	cur=0
    	for i in range (1,m):
    		pre_up=cur
    		for j in range (1,n):
    			cur = pre_up+pre_left
    			pre_left=cur
    		

    	return cur 

so =Solution()
print (so.test(3,2))