#  nums = [4,5,6,7,0,1,2], target = 0, target=3
#  4 ,-1

class Solution():
    def search(self, nums: [int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


so = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]
print(so.search(nums, 4))


class Soluiton2():
    def search(self, nums: [int], target) -> int:
        n = len(nums)
        if not nums:
            return -1
        l = 0
        r = n - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            else:
                if nums[mid] < target <= nums[n - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

so2 = Soluiton2()
print(so2.search([1,3,4], 3))
