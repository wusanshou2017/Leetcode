from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]

        res =[]

        def backtrack(start,path,s):
            if start == len(s):
                res.append(path[:])
                return 

            for i in range (1,len(s)-start+1):
                if isValid(s[start:start+i]):
                    print("isValid")
                    path.append(s[start:start+i])
                    print(path)
                else:
                    continue
                backtrack(start+i,path,s)
                path.pop()
                
        def isValid(s:str):
            if s==s[::-1]:
                return True
            return False


        backtrack(0,[],s)

        return res 
test ="aabbcddc"
so =Solution()
print(so.partition(test))
