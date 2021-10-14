
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from typing import List


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root ==None:
            return 0
        elif root.children==[]:
            return 1
        
        else:
            height  = [self.maxDepth(c) for c in root.children]
            return max(height)+1


class Solution:

    # 部分 有序
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # if len(arr)<2:
            # return -1

        l= 0 
        r = len(arr)-1
        mid = (l+r)//2
        #  二分法
        while l<r:
            mid =(l+r)//2
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid

            if arr[mid]>arr[mid-1] and arr[mid]<arr[mid+1]:
                l=mid

            if arr[mid]<arr[mid-1] and arr[mid]>arr[mid+1]:
                r=mid




class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [ [1]*n for _ in range(m)]
        print(matrix)
        for i in range(1,n):

            for j in range (1,m):
                matrix[j][i] = matrix[j-1][i]+matrix[j][i-1]

        return matrix[m-1][n-1]

so=Solution()

print(so.uniquePaths(3,7))