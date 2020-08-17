# 输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        i = 0
        res = []
        visited = []
        while i < n:
            if i in visited:
                i += 1
                continue
            pre_set = {char for char in strs[i]}
            one_group = [strs[i]]
            for j in range(i + 1, n):
                words = strs[j]
                if len(words) == len(pre_set):
                    temp_set = {char for char in words}
                    if pre_set == temp_set:
                        one_group.append(words)
                        visited.append(j)
            i += 1
            res.append(one_group)
        return res

    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:

        dict = {}
        for item in strs:
            key = tuple(sorted(item))
            dict[key] = dict.get(key, []).append[item]
        return list(dict.values())


test = ["eat", "eat", "tan", "eat", "aaa", "ate", "nat", "bat"]
so = Solution()
print(so.groupAnagrams2(test))
