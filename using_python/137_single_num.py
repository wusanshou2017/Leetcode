# input [2,2,3,2]
#  output :3
from collections import Counter
from typing import List
class Solution():
	def singleNumber1(self,nums:List[int])->int:
		hashmap = Counter(nums)
		for k in hashmap.keys():
			if hashmap[k]==1:
				return k

	def singleNumber(self,nums:List[int])->int:
		seen_once ,seen_twice = 0,0 
		for num in nums:
			pass 

		
	