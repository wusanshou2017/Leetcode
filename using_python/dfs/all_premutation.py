from typing import List


class Permutation():
    def permute(self, nums: List):
        nums.sort()

        def backTrack(visited: [], path: []):
            if len(path) == n:
                res.append(path[:])
                return

            for i in range(n):
                if nums[i] in path:
                    continue
                else:
                    visited.append(nums[i])
                    path.append(nums[i])
                    backTrack(visited, path)
                    visited.pop()
                    path.pop()

        res = []
        n = len(nums)
        backTrack([], [])
        return res

    def permute2(self, nums: List):
        def backTrack(visited: [], path: []):
            if len(path) == n:
                res.append(path[:])
                return

            for i in range(n):
                if i in visited:
                    continue
                else:
                    visited.append(i)
                    path.append(nums[i])
                    backTrack(visited, path)
                    visited.pop()
                    path.pop()

        nums.sort()
        res = []
        n = len(nums)
        backTrack([], [])
        return res


test = [1, 2, 3]
so = Permutation()
print(so.permute(test))
