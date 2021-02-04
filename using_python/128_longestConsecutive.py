# 示例 1：

# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。


from typing import List


class Unionfind:
    def __init__(self, n: int):
        self.fa = [0] * n
        self.rank = [0] * n

        for i in range(n):
            self.fa[i] = n
            self.rank[i] = 1

    def find(self, target: int):
        if target == self.fa[target]:
            return target
        else:
            return find(fa[target])

    def merge(self, i, j):
        x = find(i)
        y = find(j)
        if (self.rank[i] < self.rank[j]):
            self.fa[x] = y
        else:
            self.fa[y] = x
        if(rank[x] == rank[y] and x != y):
            rank[y] += 1


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = Unionfind(len(nums))
        m = {}
        for i in range(len(nums)):
            cur = m[i]
            if cur in m.keys():
                continue
            m[cur] = i
            if (cur - 1) in m.keys():
                uf.merge(i, m[cur - 1])
            if (cur + 1) in m.keys():
                uf.merge(i, m[cur + 1])

        res = 0
        for v in range(len(self.fa)):
            if v > res:
                res = v
        return v


so = Solution()

test_data = [100, 4, 200, 1, 3, 2]

print(so.longestConsecutive(test_data))
