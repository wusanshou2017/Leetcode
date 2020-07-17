# 输入：
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# 输出：3
A = [1, 2, 3, 2, 1]
B = [3, 2, 1, 4, 7]


class Solution:
    def test(self, A: [int], B: [int]) -> int:
        n1 = len(A)
        n2 = len(B)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]
        dp[0][0] = 0
        cand = []
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    cand.append(dp[i][j])

        if not cand:
            return 0
        else:
            return max(cand)

    def findLength(self, A: [int], B: [int]) -> int:
        n, m = len(A), len(B)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = dp[i + 1][j + 1] + 1 if A[i] == B[j] else 0
                ans = max(ans, dp[i][j])
        return ans


so = Solution()
print(so.findLength([0, 1, 1, 1, 1],
                    [1, 0, 1, 0, 1]))
