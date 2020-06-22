class Solution:
    def lengthOfLastWord(self, s: str) -> int:
    	n= len (s)
    	lst =s.split(" ")
    	res =len(lst[-1])
    	return res


    	