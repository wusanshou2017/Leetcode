#  input :[23,2,4,6,7], k = 6
#  output : True



class Solution:
    def checkSubarraySum(self, nums: [int], k: int):
		n =len(nums)
		if n < 2:
			return False
		dp = [0] * len(nums)
		dp[0] = nums[0]
		for i in range(1,len(nums)):
		    dp[i] = dp[i-1] + nums[i] #获取nums的0-i的和，包括i

		print ("dp...:",dp)
		for i in range(len(nums)-1):
		    for j in range(i+1,len(nums)):
		        sums = dp[j] - dp[i] + nums[i] #得到sums[i:j]的大小，这里包括j
		        if k == 0:
		            if sums == 0:
		                return True
		        else:
		            if sums % k == 0:
		                return True
		return False


test =[23,2,6,4,7]
k=8
so=Solution()
print (so.checkSubarraySum(test,k))
    			