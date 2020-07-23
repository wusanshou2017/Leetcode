class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        l_lst = [len(item) for item in strs]
        min_len = min(l_lst)
        n = len(strs)
        end_index = 0
        for i in range(n):
            for j in range(min_len):
                if strs[i][j] == strs[0][j]:
                    end_index = j
                else:
                    ans = strs[0][:j]
                    return ans

        return strs[0][:end_index + 1]


so = Solution()

test = ["appll", "abp", "apple"]


print(so.longestCommonPrefix(test))
