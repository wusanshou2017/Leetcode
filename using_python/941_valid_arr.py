# A.length >= 3
# 在 0 < i < A.length - 1 条件下，存在 i 使得：
# A[0] < A[1] < ... A[i-1] < A[i]
# A[i] > A[i+1] > ... > A[A.length - 1]
from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        res = []
        n = len(A)
        if n < 3:
            return False

        for i in range(1, n - 1):
            if A[i - 1] < A[i] and A[i] > A[i + 1]:
                res.append(A[i])
            if A[i - 1] >= A[i] and A[i] <= A[i + 1]:
                return False

        if A[n - 1] > A[n - 2]:
            return False
        return len(res) == 1


so = Solution()
print(so.validMountainArray([0, 1, 2, 1, 2]))
