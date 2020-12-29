from typing import List

MAX_INT = 2**31


class Solution():
    """
        docstring for  Solution":
        this class is for dp algorithm practise which is the 
        question of maxprofits

    """
    #  one dimensen array to implement dp algorithm
    #

    def maxprofit1(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        n = len(prices)
        dp = [0] * n
        low_price = prices[0]
        for i in range(1, n):
            low_price = min(low_price, prices[i])
            dp[i] = max(dp[i - 1], prices[i] - low_price)
        return dp[n - 1]

    # greedy algorithm

    def maxprofit2(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        n = len(prices)
        low_price = prices[0]
        res = 0
        for i in range(1, n):
            if prices[i] > low_price:
                res += prices[i] - low_price
                low_price = prices[i]
            #  unit_test
            else:
                low_price = min(low_price, prices[i])

        return res

    def maxprofit3(self, prices: List[int]) -> int:
        # 示例 1:
        # 输入: [3,3,5,0,0,3,1,4]
        # 输出: 6

        # 输入: [1,2,3,4,5]
        # 输出: 4

        if len(prices) < 2:
            return 0
        n = len(prices)
        count = 2
        dp = [[0] * n for _ in range(n)] * count
        for time in count:
            for i in range(n):
                for j in range(i, n):
                    dp[i][j][time] = max()


so = Solution()

test = [3, 1, 5, 7, 2, 3, 5, 7, 8, 1, 3]

print(so.maxprofit1(test))
print(so.maxprofit2(test))
