class Solution:
    def premute(self, nums):
        def backtrack(first=0):
            if first == n:
                res.append(nums[:])
            visited = set()
            for i in range(first, n):
                if nums[i] in visited:
                    continue
                nums[first], nums[i] = nums[i], nums[first]
                visited.add(nums[i])
                backtrack(first + 1)
                nums[i], nums[first] = nums[first], nums[i]
        n = len(nums)
        res = []
        backtrack()
        return res


test = [1, 2, 1, 1]

so = Solution()
print(so.premute(test))
