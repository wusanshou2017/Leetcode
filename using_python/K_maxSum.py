class Solution:
    def kConcatenationMaxSum(self, arr: [int], k: int) -> int:
        s, ans = 0, 0
        for a in arr * min(2, k):
            s = a if s < 0 else s + a
            if s > ans:
                ans = s
        if k <= 2:
            return ans

        return (max(sum(arr), 0) * (k - 2) + ans) % 1000000007

    def test(self, arr: [int], k: int) -> int:
        n = len(arr)
        s, d = [0] * (n + 1), [0] * n
        for i in range(n):
            s[i + 1] = s[i] + arr[i]  # 前缀和
            d[i] = max(d[i - 1] + arr[i], 0)  # 最大连续和


        if k == 1:
            return max(d)

        return max(max(d), max(s[n], 0) * (k - 2) + s[n] - min(s) + max(s))


so = Solution()


print(so.test([1, -2, 1], 5))
