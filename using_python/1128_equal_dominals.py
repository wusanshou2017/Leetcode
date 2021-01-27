
# 输入：dominoes = [[1,2],[2,1],[3,4],[5,6]]
# 输出：1
from typing import List


class Solution:

    # brutal force method to solve the array
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        visited = []
        count = 0
        for index1, item1 in enumerate(dominoes):
            if index1 in visited:
                continue
            for index2, item2 in enumerate(dominoes[index1 + 1:]):
                if item1 == item2 or item1 == item2[::-1]:
                    visited.append(index2)
                    count += 1

        return count

    #  to parse the pattern and decrease the  complexsity of time
    def numEquivDominoPairs2(self, dominoes: List[List[int]]) -> int:
        num = [0] * 100
        ret = 0
        for x, y in dominoes:
            val = (x * 10 + y if x <= y else y * 10 + x)
            ret += num[val]
            num[val] += 1
        return ret


so = Solution()
print(so.numEquivDominoPairs2(
    [[1, 1], [2, 2], [1, 1], [1, 2], [1, 2], [1, 1]]))





