class Solution():
	def findLengthofLcis(self,nums:[int])->int:
		n = len (nums )
		pre= nums [0]
		res =0
		for i in range (1,n):
			if nums[i]> pre:
				res+=1

		pass 
	