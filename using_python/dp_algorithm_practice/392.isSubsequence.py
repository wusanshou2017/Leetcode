# s = "abc", t = "ahbgdc"
# true.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s :
            return True 
        if s and not t:
            return  False 

        p,q =0,0
        while p<len(s) and q <len(t):
            if s[p]==t[q]:
                p+=1
                q+=1

            else :
                q+=1

        return p == len(s)
so =Solution()
print (so.isSubsequence("axc","ahbgdc"))