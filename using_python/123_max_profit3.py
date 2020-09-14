from typing import List
# 输入: [3,3,5,0,0,3,1,4]
# 输出: 6
class Solution:
    def my_maxProfit(self, prices: List[int]) -> int:
        n = len (prices)
        if n<2:
            return 0

        dp = [0] * n   
        res =0
        for i in range(1,n):
            if prices[i]>prices[i-1]:
                res+= prices[i]-prices[i-1]
                dp[i] =res
            
            
        print(dp)
        count =1
        for i in range(1,len(dp)):
            if dp[i]==0 and dp[i-1]!=0:
                count=2
        dp.sort()
        res =sum(dp[-count:])
        return res

    def maxProfit2(self, prices: List[int]) -> int:
        buy_1 = buy_2 = float('inf') # 
        pro_1 = pro_2 = 0 
        for p in prices:
            buy_1 = min (buy_1, p)
            pro_1 = max (pro_1, p - buy_1)
            buy_2 = min (buy_2, p - pro_1) 
            pro_2 = max (pro_2, p - buy_2)
        return pro_2



so = Solution()
print (so.maxProfit2([1,2,4,2,5,7,2,4,9,0])) 




