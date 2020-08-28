from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        modified = -999999

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(m):
                        matrix[k][j] = modified if matrix[k][j] != 0 else 0

                    for l in range(n):
                        matrix[i][l] = modified if matrix[i][l] != 0 else 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == modified:
                    matrix[i][j] = 0

        return
