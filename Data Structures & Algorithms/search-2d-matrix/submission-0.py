class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            first = matrix[i][0]
            if first == target:
                return True
            if i+1 < len(matrix):
                second = matrix[i+1][0]
                if target >= second:
                    continue
            row = matrix[i]
            return any(x==target for x in row)

        