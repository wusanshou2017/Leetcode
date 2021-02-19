# 输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# 输出：6
# 解释：
# [1,1,1,0,0,1,1,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 6。


from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        res, slow, fast = 0, 0, 0
        n = len(A)
        while slow < n and fast < n:
            if A[fast] or K:
                if A[fast]:
                    K -= 1
                fast += 1
            else:
                if A[slow]:
                    fast += 1
                slow += 1
            res = max(res, fast - slow)
        return res


test_data = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
K = 2
so = Solution()

print(so.longestOnes(test_data, K))
