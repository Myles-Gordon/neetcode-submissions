class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        matrix = [[0 for _ in range(cols+1)] for _ in range(rows+1)]

        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if text1[i] == text2[j]:
                    matrix[i][j] = 1+matrix[i+1][j+1]
                else:
                    matrix[i][j] = max(matrix[i][j+1], matrix[i+1][j])
        
        return matrix[0][0]