class Solution:
    def premute(self, nums):
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path[:])
                return res

            for i in range(size):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        continue
                    used[i] = True
                    path.append(nums[i])
                    dfs(nums, size, depth + 1, path, used, res)
                    used[i] = False
                    path.pop()

                else:
                    continue

        size = len(nums)
        if size == 0:
            return []
        used = [False for _ in range(size)]
        nums.sort()
        res = []
        dfs(nums, size, 0, [], used, res)
        return res


test = [1, 2, 1, 1]

so = Solution()
print(so.premute(test))
