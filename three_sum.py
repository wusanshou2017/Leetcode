# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

# 满足要求的三元组集合为：
# [
#     [-1, 0, 1],
#     [-1, -1, 2]
# ]

class Solution:
    def three_sum(self, nums: [int]) -> [[int]]:
        if len(nums) < 3:
            return [[]]

        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            sub_target = 0 - nums[i]
            for j in range(i + 1, n):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, n):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    if nums[j] + nums[k] == sub_target:
                        res.append([nums[i], nums[j], nums[k]])

        return res

    def three_sum2(self, nums: [int]) -> [[int]]:
        n = len(nums)
        res = []
        if(not nums or n < 3):
            return []
        nums.sort()
        res = []
        for i in range(n):
            if(nums[i] > 0):
                return res
            if(i > 0 and nums[i] == nums[i - 1]):
                continue
            L = i + 1
            R = n - 1
            while(L < R):
                if(nums[i] + nums[L] + nums[R] == 0):
                    res.append([nums[i], nums[L], nums[R]])
                    while(L < R and nums[L] == nums[L + 1]):
                        L = L + 1
                    while(L < R and nums[R] == nums[R - 1]):
                        R = R - 1
                    L = L + 1
                    R = R - 1
                elif(nums[i] + nums[L] + nums[R] > 0):
                    R = R - 1
                else:
                    L = L + 1
        return res


nums = [-1, 0, 1, 2, -1, -4]

so = Solution()

print(so.three_sum(nums))
