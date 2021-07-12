class Solution:
    def three_sum(self, nums):
        nums=sorted(nums)
        res=[]
        if (len (nums)<3 or nums[0]>0 or nums[len(nums) - 1]<0):
            return []
        n=len(nums)
        dic_sum_index={}
        for i in range(n):
            j=i+1
            while j<n:
                dic_sum_index[[i,j]]=nums[i]+nums[j]
                j+=1
        for idx,num in enumerate(nums):
            if -num in dic_sum_index.values():
                if idx not in dic_sum_index[-num]:
                    temp_index =dic_sum_index[-num]
                    temp=[]
                    for index in temp_index:
                        temp.append(nums[index])
                    temp.append(num)
                    temp=sorted(temp)
                    if temp not in res:
                        res.append(temp)


        return res

# so=Solution()
# res =so.three_sum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]);
# print(res)

t={}
t["1"]=1
t["1"]=2
print(t)