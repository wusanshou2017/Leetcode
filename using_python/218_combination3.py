class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candidates = [i for i in range(1, 10)]
        res = []

        def backTrack(visited, path, start):
            if (len(path) == k):
                if (sum(path) == n):
                    res.append(path[:])
                return
            for i in range(start, 10):
                if i in visited:
                    continue
                visited.append(i)
                path.append(i)
                backTrack(visited, path, i)
                visited.pop()
                path.pop()
        backTrack([], [], 1)
        return res
