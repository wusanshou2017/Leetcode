class Solution:
    def isPalindrome(self, x: int) -> bool:
        nums = x
        lst = []
        while nums > 0:
            m = nums % 10
            nums = nums // 10
            lst.append(m)
        n = len(lst)
        res = 0
        for i in range(n):
            temp = 1
            for j in range(n - 1 - i):
                temp = 10 * temp
            res += temp * lst[i]
        return res == x


so = Solution()
print(so.isPalindrome(12321))
