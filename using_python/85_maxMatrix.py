# input:[
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# output: 6


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[1] * n for _ in range(m)]
        dp[0] = [for i in range(1, n + 1)]
        for i in range(m):
            dp[i][0] = i + 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] =
        