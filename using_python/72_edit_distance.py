class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        matrix = [[i + j for j in range(len(word2) + 1)]
                  for i in range(len(word1) + 1)]
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    d = 0
                else:
                    d = 1
                matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i]
                                   [j - 1] + 1, matrix[i - 1][j - 1] + d)

        return matrix[len(word1)][len(word2)]
