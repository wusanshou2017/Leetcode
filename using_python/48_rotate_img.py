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
        n = len(matrix[0])
        # transpose matrix
        for i in range(n):
            for j in range(i, n):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

        # reverse each row
        for i in range(n):
            matrix[i].reverse()

    def my_rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)

        temp_matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                temp_matrix[j][n - i - 1] = matrix[i][j]

        matrix = temp_matrix
        print(matrix)


m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

so = Solution()
so.rotate(m)
