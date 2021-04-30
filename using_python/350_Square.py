# a ^ 2 + b ^ 2 == c ^ 2
import math


class Solution:
    def isSquare(self, c: int):
        srt = int(math.sqrt(c))
        candidates = [num for num in range(0, srt + 1)]
        left = 0
        right = len(candidates) - 1

        while left <= right:
            num1 = candidates[left]
            num2 = candidates[right]
            if (num1 * num1 + num2 * num2) < c:
                left += 1
            elif (num1 * num1 + num2 * num2) == c:
                return True
            else:
                right -= 1
        return False
