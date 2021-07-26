
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        total_nums = len(nums1) * len(nums2)

        if k > total_nums:
            result = [[item1, item2] for item1 in nums1 for item2 in nums2]
            return result
        idx_res = []
        sum_res = []
        idx_sum_lst = []
        for index1, item1 in enumerate(nums1):
            for index2, item2 in enumerate(nums2):
                sum_res.append(item1 + item2)
                idx_res.append((index1, index2))
                idx_sum_lst.append((index1, index2, item1 + item2))

        res_idx_sum = sorted(idx_sum_lst, key=lambda x: (x[2]))
        print(res_idx_sum)
        # import heapq
        # sum_res = [-item for item in sum_res]
        # heapq.heapify(sum_res)
        result = []
        for i in range(k):

            result.append([nums1[res_idx_sum[i][0]], nums2[res_idx_sum[i][1]]])
        # res = []
        # result = []
        # for _ in range(k):
        #     temp = heapq.heappop(sum_res)
        #     print(sum_res)
        #     res.append(temp)
        # print(res)

        # for two_sum in res:
        #     for item in idx_sum_lst:
        #         if item[2] == two_sum:
        #             result.append([nums1[item[0]], nums2[item[1]]])

        return result

from heapq import heappop, heappush

class MySolution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res, q = [], []
        if len(nums1) == 0 or len(nums2) == 0 or k == 0:
            return res
        for i in range(k):
            if i >= len(nums1):
                break
            heappush(q, (nums1[i] + nums2[0], nums1[i], 0))
        while k and q:
            cur = heappop(q)
            res.append([cur[1], cur[0] - cur[1]])
            k -= 1
            if cur[2] == len(nums2) - 1:
                continue
            heappush(q, (cur[1] + nums2[cur[2] + 1], cur[1], cur[2] + 1))
            
        return res



so = Solution()

# [1,2,4,5,6]
# [3,5,7,9]

nums1 = [1, 2, 4, 5, 6]
nums2 = [3, 5, 7, 9]

print(so.kSmallestPairs(nums1, nums2, 3))
