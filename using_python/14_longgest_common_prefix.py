class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:

        if not strs:
            return ""
        if "" in strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        nums_str = len(strs)
        end_index = len(strs[0])
        for item in strs[1:]:
            end_index = min(end_index, self.compare_two_str(strs[0], item))

        return strs[0][:end_index]

    def compare_two_str(self, str1, str2):
        n = min(len(str1), len(str2))
        index = 0
        for i in range(n):
            if str1[i] != str2[i]:
                break
            else:
                index += 1
        return index


so = Solution()

test = ["appll", "app", "apple"]


print(so.longestCommonPrefix(test))
