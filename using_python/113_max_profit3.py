from typing import List
# 输入: [3,3,5,0,0,3,1,4]
# 输出: 6
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    	n = len (prices)
    	if n<2:
    		return 0

    	dp = [0] * n   
    	
    	for i in range(1,n):
    		if prices[i]>prices[i-1]:
    			dp[i]+= prices[i]-prices[i-1]+dp[i-1]
    		
    	print(dp)
    	dp.sort()
    	res =dp[-1]+dp[-2]
    	return res


so = Solution()
print (so.maxProfit([3,3,5,0,0,3,1,4])) 




