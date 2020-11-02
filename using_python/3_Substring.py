class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        if n < 2:
            return n
        slow_ptr, fast_ptr = 0, 1
        res = 0
        while slow_ptr < n and fast_ptr < n:
            print (s[slow_ptr:fast_ptr])
            if s[fast_ptr] in s[slow_ptr:fast_ptr]:
                res = max(res, fast_ptr - slow_ptr)
                slow_ptr += 1
            else:
                res = max(res, fast_ptr - slow_ptr)
                fast_ptr += 1
        if slow_ptr == 0 and fast_ptr == n:
            return n
        return res


so = Solution()
print(so.lengthOfLongestSubstring("bbbbb"))
