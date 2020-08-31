from typing import List
class Solution():
	def my_combine(self, n: int, k: int) -> List[List[int]]:
		assert(k<n)
		res=[]
		nums =[i for i in range (n)]
		path =[]
		size =k
		def dfs(res,path,depth,size,nums,used):
			
			if depth==size:
				res.append(path[:])
				return 

			for i in range(size):
				if not used[i]:
					used[i]=True
					path.append()
					dfs(res,path,depth+1,size,nums)
					path.pop


		return res 

	def combine(self,n:int ,k:int)->List[List[int]]:
		res =[]
		def back_track(first=1,curr=[]):
			if len(curr)==k:
				res.append(curr[:])
				return
			for i in range(first,n+1):
				curr.append(i)
				back_track(i+1,curr)
				curr.pop()
		back_track()
		return res


so =Solution()
print (so.combine(4,2))

		