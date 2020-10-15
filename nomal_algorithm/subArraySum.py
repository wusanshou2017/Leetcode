from typing import List

import random

# two ways to calculate the max sum of subarray

# time: O(n)
# space: O(n)


def subArray(nums: List[int]) -> int:
    if not nums:
        return -1
    pre = nums[0]
    ans = nums[0]
    for i in range(1, len(nums)):
        pre = max(pre, pre + nums[i])
        ans = max(ans, pre)
        if nums[i] < 0:
            pre = 0

    return ans

# unit_test
# time: O(n)
# space: O(n)


def dp_subArray(nums: [int]) -> int:
    min_num = - 2**16
    dp = [min_num] * len(nums)
    dp[0] = nums[0]
    for i in range(1, len(nums)):
        if nums[i] >= 0:
            dp[i] = nums[i] + dp[i - 1]
        else:
            dp[i] = 0
    return max(dp)

# for unit_test to verify the algorithm is right or not


if __name__ == '__main__':
    for _ in range(1000):
        nums = [random.randint(-100, 100) for i in range(10000)]

        assert (subArray(nums) == dp_subArray(nums))
    print("finish....")
