# 输入: 3
# 输出:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]


from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        matrix = [[0] * n for _ in range(n)]

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        visted = [[0, 0]]
        matrix[0][0] = 1
        pre_index = [0, 0]
        direct = 0
        for i in range(2, n * n + 1):
            temp = pre_index
            pre_index = [pre_index[0] + directions[direct]
                         [0], pre_index[1] + directions[direct][1]]
            if pre_index[0] < n and pre_index[0] >= 0 and pre_index[1] < n and pre_index[1] >= 0 and pre_index not in visted:
                matrix[pre_index[0]][pre_index[1]] = i
                visted.append(pre_index)

            else:
                direct += 1
                if direct > 3:
                    direct = 0
                pre_index = temp
                pre_index = [pre_index[0] + directions[direct]
                             [0], pre_index[1] + directions[direct][1]]

                matrix[pre_index[0]][pre_index[1]] = i
                visted.append(pre_index)

        return matrix


so = Solution()
print(so.generateMatrix(3))
