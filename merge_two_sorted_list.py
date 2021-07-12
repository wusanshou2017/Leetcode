import re
# 输入:
# nums1 = [1,2,3,0,0,0], m = 6
# nums2 = [2,5,6],       n = 3

# 输出: [1,2,2,3,5,6]


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        nums1_copy = nums1[:m]
        nums1[:] = []
        p1 = 0
        p2 = 0
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1.append(nums1_copy[p1])
                p1 += 1
            else:
                nums1.append(nums2[p2])
                p2 += 1

        if p1 < m:
            nums1[p2 + p1:] = nums1_copy[p1:]
        if p2 < n:
            nums1[p1 + p2:] = nums2[p2:]
        print(nums1)


s = "我是一个人(中国人)aaa[真的]bbbb{确定}"
a = re.sub(u"\\(.*?\\)|\\{.*?}|\\[.*?]", "", s)
print(a)
