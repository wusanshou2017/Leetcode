# 输入：k = 2, prices = [2,4,1]
# 输出：2
# 输入：k = 2, prices = [3,2,6,5,0,3]
# 输出：7

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        dp = [ [0] * n for _ in range (n)]
        for i in range (n-1):
            for j in range (i+1,n):
                dp[i][j] = max(prices[j]-prices[i]+dp[i])
                if dp[i][j]>0:
                    pass
                else:
                    pass
                    
        return dp[n][n]
