from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    	res =0
    	n =len(prices)
    	if n<2:
    		return res 
    	for i in range(1,n):
    		if prices[i]>prices[i-1]:
    			res+= prices[i]-prices[i-1]

    	return res 


so =Solution()

print(so.maxProfit([1,5,3,4,5]))