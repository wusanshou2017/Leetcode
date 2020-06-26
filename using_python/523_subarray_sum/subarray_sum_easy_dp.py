class Solution():
	def subarray(self, nums:[], k:int):
		n =len (nums )
		if n<2:
			return False
		dp =[0]* (n+1)
		total =0
		for i in range (n):
			total+= nums[i]
			dp[i+1] = total
		print ("dp...:",dp)

		for j in range (n+1):
			for m in range (j-1):
				if k==0:
					return True 
				print (dp[j]-dp[m])
				if (dp[j]-dp[m])% k==0:
					print ("sum:...",dp[j]-dp[m])
					return True

		return False

test =[23,2,4,6,7]
k= 42
so =Solution()
print (so.subarray(test,k))

			