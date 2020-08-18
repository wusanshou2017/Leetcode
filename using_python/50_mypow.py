class Solution:
	def myPow(self,x:float,n:int)->float:
		def quick_mul(N):
			if N ==0:
				return 1.0
			y =quick_mul(N//2)
			return y*y if N %2==0 else y*y*x

		return quick_mul(n) if n>=0 else 1.0/quick_mul(-n)
