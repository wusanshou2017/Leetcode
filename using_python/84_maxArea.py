#  [2,1,5,6,2,3]
#  10

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        for i in range(n):
            for j in range(i + 1, n):
                h = min(heights[i], heights[j])
                max_area = max((j - i + 1) * h, max_area)
        return max_area


so = Solution()
print(so.largestRectangleArea([2, 1, 5, 6, 2, 3]))


s1 = "[1231]sdf"

l = [1, 2, 4, 5, 6]

l[2:4] = [0, 0]
print(l)
