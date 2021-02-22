# 输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# 输出：6
# 解释：
# [1,1,1,0,0,1,1,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 6。
#
#
# int longestOnes(int* A, int ASize, int K) {
#     int res = 0;
#     int i = 0, j = 0;
#     while(i < ASize && j < ASize) {
#         if(A[j] || K )
#             A[j++]? : K--;
#         else
#             A[i++]? : j++;

#         res = res > j - i? res: j - i;
#     }
#     return res;
# }
# class Solution {
# public:
#     int longestOnes(vector<int>& A, int K) {
#         int res = 0;
#         int l = 0, r = 0;
#         while(l < A.size() && r < A.size()){
#             if(A[r] || K){
#                if(A[r] == 0){

#                    K--;
#                }
#                r++;
#             }
#             else{

#                 if(A[l] == 0){

#                     r++;
#                 }
#                 l++;
#             }
#             res = res > r - l ? res : r - l;
#         }
#         return res;
#     }
# };

from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        res, slow, fast = 0, 0, 0
        k = K
        n = len(A)
        while slow < n and fast < n:

            if A[fast] or k:
                if A[fast] == 0:
                    k -= 1
                fast += 1

            else:                
                if A[slow] == 0:
                    fast += 1
                slow += 1

            res = max(res, fast - slow)
        return res

test_data = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]

K = 2

so = Solution()

print(so.longestOnes(test_data, K))
