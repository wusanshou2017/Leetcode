class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        temp_lst1=[]
        temp_lst2=[]
        for num in A:
            if num%2==0:
                temp_lst2.append(num)
            else:
                temp_lst1.append(num)
        res=[]
        i,j=0,0
        n = len(A)
        for k in range(n):
            if k%2==0:
                res.append(temp_lst2[i])
                i+=1
            else:
                res.append(temp_lst1[j])
                j+=1
        return res 