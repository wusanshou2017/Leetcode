
class Solution:
    def test(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n):
            dp[i][i + 1] = i

        for low in range(n - 1, 0, -1):
            for high in range(low + 1, n + 1):

                dp[low][high] = min(
                    x + max(dp[low][x - 1], dp[x + 1][high]) for x in range(low, high))
                print("dp[][]...:", dp[low][high])
                print("low , high...:", [low, high])

        return dp[1][n]

    def getAmount(self, n: int) -> int:
        for i in range(1, n):
            dp[i][i + 1] = i

            pass


test = 0
so = Solution()
print(so.test(6))
