# 输入: nums = [0, 1, 3, 50, 75], lower = 0 和 upper = 99,
# 输出: ["2", "4->49", "51->74", "76->99"]


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        r = []
        nums = [lower - 1] + nums + [upper + 1]
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 2:
                r.append(str(nums[i - 1] + 1) + '->' + str(nums[i] - 1))
            elif nums[i] - nums[i - 1] == 2:
                r.append(str(nums[i] - 1))
        return r
