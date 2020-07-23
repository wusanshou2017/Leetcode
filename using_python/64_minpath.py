# 输入:
# [
#   [1,3,1],
#   [1,5,1],
#   [4,2,1]
# ]
# 输出: 7

class Solution:
    def minPathSum(self, grid: [[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[65535] * n for _ in range(m)]
        dp[0][0] = grid[0][0]
        ### dp[i][j] = min(dp[i][j-1],dp[i-1][j])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                dp[i][j] = grid[i][j] + min(dp[i][j - 1], dp[i - 1][j])

        return dp[-1][-1]


test = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
so = Solution()
print(so.minPathSum(test))
