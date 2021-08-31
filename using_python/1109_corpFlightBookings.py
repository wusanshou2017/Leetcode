
# 这里有 n 个航班，它们分别从 1 到 n 进行编号。

# 有一份航班预订表 bookings ，表中第 i 条预订记录 bookings[i] = [firsti, lasti, seatsi] 意味着在从 firsti 到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi 个座位。

# 请你返回一个长度为 n 的数组 answer，其中 answer[i] 是航班 i 上预订的座位总数。

from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:


        # m = len(bookings)
        # matrix = [ ([0]* n ) for _ in range(m)]
        # print(matrix)
        # for i in range(m):
        #     start_indx = bookings[i][0]-1
        #     end_indx = bookings[i][1]-1
        #     # for j in range(start_indx,end_indx+1):
        #         # matrix[i][j] = bookings[i][2]
        #     matrix[i][start_indx:end_indx+1] = [bookings[i][2]]* (end_indx+1-start_indx) 

        #     # matrix[i][bookings[i][0]-1]= bookings[i][2]
        #     # matrix[i][bookings[i][1]-1]= bookings[i][2]

        # print(matrix)
        # ans =[]

        # # for j in range(n):

        # #     temp =0 
        # #     for i in range(m):
        # #         temp += matrix[i][j]


   
        # # for j in range(n):

        # #     ans.append(sum(matrix[:][j]))

        # # return ans 


        nums = [0] * n
        for left, right, inc in bookings:
            nums[left - 1] += inc
            if right < n:
                nums[right] -= inc
        
        for i in range(1, n):
            nums[i] += nums[i - 1]
        
        return nums

#  unit test
if __name__ == '__main__':

    bookings = [[1,2,10],[2,3,20],[2,5,25]]
    # bookings = [[1,2,10],[2,2,15]]
    n = 5
    so =Solution()

    print(so.corpFlightBookings(bookings,n))            



                # [10,55,45,25,25]