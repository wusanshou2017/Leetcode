class Soluiton:
	def maxSubArray(self,nums:[int])->int:
		pre ,res  = 0 ,nums[0]
		n = len (nums )
		for i in range(n):
			pre = max (nums[i]+pre,nums[i])
			res = max (res,pre)
		return res 

so =Soluiton()
test =[-2,1,-3,4,-1,2,1,-5,4]
print (so.maxSubArray(test))
