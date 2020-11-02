class Solution():
	def videoStitching(c:List[List[int]],t:int):
		n = len(c)
		tmp = sorted(c,key=(lambda x:[x[0],x[1]]))
		l,r =0,0 
		res,i=0,0
		while r<t and i<n:
			
