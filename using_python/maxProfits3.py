# 给定一个整数数组 prices，其中第 i 个元素代表了第 i 天的股票价格 ；非负整数 fee 代表了交易股票的手续费用。

# 你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

# 返回获得利润的最大值。

# 注意：这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

# 示例 1:

# 输入: prices = [1, 3, 2, 8, 4, 9], fee = 2
# 输出: 8
# 解释: 能够达到的最大利润:
# 在此处买入 prices[0] = 1
# 在此处卖出 prices[3] = 8
# 在此处买入 prices[4] = 4
# 在此处卖出 prices[5] = 9
# 总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
# unit_test to be done


print("unit_test ")

INT_MAX = 2**32


class Solution():
    def get_max(self, nums: [int], fee: int) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = 0
        low_price = nums[0]
        for i in range(1, n):
            low_price = min(low_price, nums[i])
            dp[i] = max(dp[i - 1], nums[i] - low_price - fee)

        return dp[n - 1]

    def maxProfit(self, prices: [int], fee: int) -> int:
        n = len(prices)
        dp = [0] * n
        dp[0] = 0
        low_price = prices[0]

        low_price_index = 0

        for i in range(1, n):
            print(low_price)
            dp[i] = max(dp[i - 1], dp[i - 1] + prices[i] - low_price - fee)
            if dp[i] > dp[i - 1]:
                low_price_index += 1
                low_price = prices[low_price_index]

        return dp[n - 1]

    def uniform_the prices(self,nums:[int],fee:int)->int :
        n  =len(nums)
        dp = [ [0] * n for _ in range(n)]

        
        dp[0][0] =0



# unit_test
#
# [1,3,7,5,10,3]
# 3
# expect: 6


so = Solution()

print("res...", so.maxProfit([1, 3, 7, 5, 10, 3], 3))
