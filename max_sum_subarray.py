"""
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
"""


def max_sum_subarray(nums: [int]) -> int:
    pre, res = 0, nums[0]
    for i in range(len(nums)):
        pre = max(nums[i], pre + nums[i])
        res = max(res, pre)

    return res


print(max_sum_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

# int pre = 0, maxAns = nums[0];
#        foreach (int x in nums) {
#            pre = Math.Max(pre + x, x);
#            maxAns = Math.Max(maxAns, pre);
#        }
#        return maxAns;
