class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        assert(len(pattern) == len(s))
        temp_lst = s.split(" ")

        dic_temp = {c: s for c, s in zip(pattern, temp_lst)}
        for i in range(len(pattern)):
            if temp_lst[i] != dic_temp[pattern[i]]:
                return False
        return True
