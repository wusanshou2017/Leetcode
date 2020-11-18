class Solution:
    def reverse(self, x: int) -> int:
        Min_Int = -2**31
        Max_Int = 2**31-1
        s= str(x)
        if s[0]=="+":
            res = int(s[-1:0:-1])
            return res if Min_Int<res<Max_Int else 0
        elif s[0]=="-":
            res = int(s[-1:0:-1])
            return -res if Min_Int<res<Max_Int else 0

        else:
            res = int(s[::-1])
            return res if Min_Int<res<Max_Int else 0