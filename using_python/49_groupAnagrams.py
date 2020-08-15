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

            temp_set = {char for char in strs[i]}

            j = i + 1
            one_group = [strs[i]]
            while j < n:
                words = strs[j]
                if len(words) == len(temp_set):
                    temp_set2 = {char for char in words}
                    if temp_set == temp_set2:
                        one_group.append(words)
                        visited.append(j)
                j += 1

            i += 1

            res.append(one_group)

        return res


test = ["eat", "eat", "tea", "tae", "ate", "nat", "bat"]

so = Solution()

print(so.groupAnagrams(test))


l1 = [["hos"], ["boo"], ["nay"], ["deb", "deb"], ["wow"], ["bop"], ["bob"], ["brr"], ["hey"], ["rye"], ["eve"], ["elf"], ["pup"], ["bum"], ["iva"], ["lyx"], ["yap"], ["ugh", "ugh"], ["hem"], ["rod"], ["aha"], ["nam"], [
    "gap"], ["yea"], ["doc"], ["pen"], ["job"], ["dis"], ["max"], ["oho"], ["jed"], ["lye"], ["ram"], ["pup"], ["qua"], ["mir"], ["nap"], ["hog"], ["let"], ["gym"], ["bye"], ["lon"], ["aft"], ["eel"], ["sol"], ["jab"]]

l2 = [["sol"], ["wow"], ["gap"], ["hem"], ["yap"], ["bum"], ["ugh", "ugh"], ["aha"], ["jab"], ["eve"], ["bop"], ["lyx"], ["jed"], ["iva"], ["rod"], ["boo"], ["brr"], ["hog"], ["nay"], ["mir"], ["deb", "deb"], ["aft"], [
    "dis"], ["yea"], ["hos"], ["rye"], ["hey"], ["doc"], ["bob"], ["eel"], ["pen"], ["job"], ["max"], ["oho"], ["lye"], ["ram"], ["nap"], ["elf"], ["qua"], ["pup", "pup"], ["let"], ["gym"], ["nam"], ["bye"], ["lon"]]

l1 = l1.sort()
l2 = l2.sort()

print(l1)
print(l2)
