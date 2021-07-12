class Solution:
    def get_max(self,target):
        n=len(target)
        left=0
        right =n-1
        max_area=0
        while left<right:
            if target[left]<target[right]:
                temp_area=target[left]*(right-left)
                max_area=max(max_area,temp_area)
                left+=1

            if target[right]<=target[left]:
                temp_area=target[right]*(right-left)
                max_area = max(max_area, temp_area)
                right-=1

        return max_area



so=Solution()
target=[1,1,1,99,1,1,1,1,100,1]
res =so.get_max(target)
print (res)