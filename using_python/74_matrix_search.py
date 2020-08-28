from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix and matrix[0]:
            for lst in matrix:
                if lst[0] <= target and target <= lst[-1]:
                    for nums in lst:
                        if nums == target:
                            return True
        return False

    def binarysearch(self, matrix: List[List[int]], target: int) -> bool:

        if matrix and matrix[0]:
            m = len(matrix)
            n = len(matrix[0])
            l = 0
            r = m * n - 1
            while l <= r:
                mid = (l + r) // 2
                print(mid // n)
                print(mid % m)
                if matrix[mid // n][mid % n] < target:
                    l = mid + 1
                elif matrix[mid // n][mid % n] > target:
                    r = mid - 1
                else:
                    return True

        return False


so = Solution()


print(so.binarysearch([[1, 3]], 3))
