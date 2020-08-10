class Solution:

    # force-brutal solution
    # def palindromePairs(self, words: List[str]) -> List[List[int]]:
    #     n =len (words)
    #     res =[]
    #     for i in range (n):
    #         for j in range (i+1,n):
    #             str_concact = words[i]+words[j]
    #             if str_concact==str_concact[::-1]:
    #                 res.append([i,j])
    #             str_concact_reverse = words[j]+words[i]
    #             if str_concact_reverse==str_concact_reverse[::-1]:
    #                 res.append([j,i])

    #     return res
    def palindromePairs(self, words: [str]) -> [[int]]:
        
        
