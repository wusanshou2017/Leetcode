# 输入: [1,2,2]
# 输出:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res =[[]]
        path =[]
        n = len(nums)
        def dfs(start,end,nums,path,res):
            for i in range(start,end):
                if i>start and nums[i]==nums[i-1]:
                    continue
                path.append(nums[i])
                res.append(path[:])
                dfs(i+1,end,nums,path,res)
                path.pop()


        dfs(0,n,nums,path,res)
        return res 


so =Solution()
print(so.subsetsWithDup([1,2,2]))




