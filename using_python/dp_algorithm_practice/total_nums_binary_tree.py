class Solution():
    """docstring for ClassName"""

    def cal_total_nums(self, nums):
        n = nums
        G = [0] * (n + 1)
        G[0], G[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]
        return G[n]


so = Solution()
print(so.cal_total_nums(4))
