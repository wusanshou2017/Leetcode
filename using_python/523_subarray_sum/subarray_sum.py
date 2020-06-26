class Solution():
	def check_subarray_sum(self , nums:[int], k:int)->bool:
		total =0 
		sum_of_subarray={0:-1}
		n =len (nums)
		for i in range (n):
			total += nums[i]
			if k != 0:
				total = total %k
			if sum_of_subarray.get(total):
				if (i - sum_of_subarray.get(total)>1):
					print ("in case sum_of_subarray")
					return True
				else:
					return False
		return False


test =[23,2,6,4,7]
k=6
so =Solution()
print (so.check_subarray_sum(test ,9))

