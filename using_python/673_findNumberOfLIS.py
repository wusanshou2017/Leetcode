# 输入: [1,3,5,4,7]
# 输出: 2
# 输入: [2,2,2,2,2]
# 输出: 5

class Solution:
	def findNumberOfLIS(self, nums: [int]) -> int:
		if not nums:
			return 0
		n= len(nums)
		length = [1]*n
		counter =[1]*n

		for i in range (1,n):
			for j in range(i):
				if nums[j]<nums[i]:
					if length[j]+1 >length[i]:
						length[i] =length[j]+1
						counter[i] =length[j]
					elif length[j]+1 ==length[i]:
						counter[i] =counter[i]+ counter[j]
		temp =max(length)
		res =sum([counter[i] for i in range(n) if length[i] ==temp ])

		return res 

so =Solution()
print (so.findNumberOfLIS([1,3,5,4,7]))
