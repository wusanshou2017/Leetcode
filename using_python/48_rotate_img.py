#
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],

#
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
#
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(n - i):
                matrix[i][j], matrix[j][n - 1 -
                                        i] = matrix[j][n - 1 - i], matrix[i][j]

        return matrix


m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

so = Solution()
print(so.rotate(m))
