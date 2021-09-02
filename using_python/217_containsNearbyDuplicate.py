

class Solution:
    def containsNearbyDuplicate(self,nums:[],k:int):
        m={}
        n = len(nums)

        for i in range(n):
            if nums[i] in m.keys() and i-m[i]<=k:
                return True

            else:
                m[nums[i]]=i

        return False


so =Solution()
test_lst = [1,2,3,1]

print( so.containsNearbyDuplicate(test_lst,3))