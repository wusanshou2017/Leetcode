# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

class Solution:

    def nextPermutation(self, nums: [int]):
         # 用于原地反转nums中从start之后的所有元素
        def reverse(nums, start):
            i, j = start, len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        # 从右到左找到第一次断崖
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 从右到左找到比崖底水平面高的第一个元素
        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # 反转
        reverse(nums, i + 1)
        return nums


class Solution2 ():

    def nextPermutation(self, nums: [int]):
        def reverse(nums, start):
            i, j = start, len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        reverse(nums, i + 1)
        return nums



so = Solution2()
test1 = [6, 5, 4, 3, 2, 1]
print(so.nextPermutation(test1))
test1 = [6, 5, 4, 3, 2, 1]
so = Solution()
print(so.nextPermutation(test1))
