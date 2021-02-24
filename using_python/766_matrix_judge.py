# class Solution:
#     def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
#         m = len(matrix)
#         n = len(matrix[0])
#         index_lst = []

#         # 主对角线
#         for i, j in zip(range(m), range(n)):
#             index_lst.append([i, j])
#             #  找子对角线

#         for i in range(m - 1):
#             if matrix[i][:-1] != matrix[i + 1][1:]:
#                 return False
#         return True





s ="/home/tdwu/workspace/deployment/pull_keywords_deployment/models/ke1xun4jia1lian2.keywords.da4ping2yu3yin1diao4du4/"



print(len(s))