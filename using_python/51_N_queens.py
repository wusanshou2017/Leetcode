from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def backtrack(row: int):
            if row == n:
                board = generateBoard()
                solutions.append(board)
            else:
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    queens[row] = i
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)

        solutions = list()
        queens = [-1] * n
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        row = ["."] * n
        backtrack(0)
        return solutions

    def solveNQueens2(self, n: int) -> List[List[str]]:

        def backTrack(row, path):
            if row == n:
                temp = ["".join(item) for item in path]
                res.append(temp[:])

            for i in range(n):
                if i in columns or row - i in diag1 or row + i in diag2:
                    continue
                path[row][i] = "Q"
                columns.add(i)
                diag1.add(row - i)
                diag2.add(row + i)
                backTrack(row + 1, path)
                path[row][i] = "."
                columns.remove(i)
                diag1.remove(row - i)
                diag2.remove(row + i)
        res = []
        columns = set()
        diag1 = set()
        diag2 = set()
        path = [["."] * n for _ in range(n)]
        backTrack(0, path)
        return res


so = Solution()
assert(so.solveNQueens(5) == so.solveNQueens2(5))
