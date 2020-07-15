test=[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]


test1=[[-10]]
class Solution:
    def minimumTotal(self, triangle: [[int]]) -> int:
        n = len (triangle)
        dp = [[0]*n for _ in range (n)]
        dp [0][0] = triangle[0][0]
        for i in range (1,n):
            dp [i][0] = dp[i-1][0]+triangle[i][0]
            for j in range(1,i):
                dp[i][j] = min(dp[i-1][j-1],dp[i-1][j])+triangle[i][j]

            dp[i][i] = dp[i-1][i-1]+triangle[i][i]

        return min (dp[n-1]) 

         

so = Solution()
print (so.minimumTotal(test1 ))

