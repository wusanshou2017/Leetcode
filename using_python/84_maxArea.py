#  [2,1,5,6,2,3]
#  10

from typing import List


class Solution:
    def force(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 1:
            return heights[0]
        max_area = 0
        for i in range(n):
            for j in range(i, n):
                h = min(heights[i:j + 1])
                max_area = max((j - i + 1) * h, max_area)
        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        res = 0
        heights = [0] + heights + [0]
        # 先放入哨兵结点，在循环中就不用做非空判断
        stack = [0]
        size += 2

        for i in range(1, size):
            while heights[i] < heights[stack[-1]]:
                cur_height = heights[stack.pop()]
                cur_width = i - stack[-1] - 1
                res = max(res, cur_height * cur_width)
            stack.append(i)
        return res

    def cal_maxArea(self, heights: List[int]):
        size = len(heights)
        res = 0
        heights = [0] + heights + [0]
        stack = [0]
        size += 2
        for i in range(1, size):
            while heights[i] < heights[stack[-1]]:
                cur_height = heights[stack[-1]]
                cur_width = i - stack[-1] - 1
                res = max(res, cur_height * cur_width)
            stack.append(i)
        return res


so = Solution()
print(so.cal_maxArea([2, 1, 5, 1, 2, 3]))
