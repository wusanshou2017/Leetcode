# 输入：[[1,1,0],[1,0,1],[0,0,0]]
# 输出：[[1,0,0],[0,1,0],[1,1,1]]
# 解释：首先翻转每一行: [[0,1,1],[1,0,1],[0,0,0]]；
#      然后反转图片: [[1,0,0],[0,1,0],[1,1,1]]


from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for i in range(len(A)):
            A[i] = A[i][::-1]

            for j in range(len(A[i])):
                if A[i][j] == 0:
                    A[i][j] = 1
                    continue
                elif A[i][j] == 1:
                    A[i][j] = 0

        return A

    def slove(self, A: List[List[int]]) -> List[List[int]]:
        A = [item[::-1] for item in A]
        m, n = len(A), len(A[0])

        for i in range(m):
            for j in range(n):
                if A[i][j] == 0:
                    A[i][j] = 1
                elif A[i][j] == 1:
                    A[i][j] = 0

        return A


so = Solution()
print(so.flipAndInvertImage([[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
