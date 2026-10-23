class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1
        row = []
        while start <= end:
            k = start + (end - start)//2
            if matrix[k][0] <= target and matrix[k][-1] >= target:
                row = matrix[k]
                break
            elif target < matrix[k][0]:
                end = k - 1
            elif target > matrix[k][-1]:
                start = k + 1
        
        start = 0
        end = len(row) - 1
        while start <= end:
            k = start + (end - start)//2
            if row[k] > target:
                end = k-1
            elif row[k] < target:
                start = k+1
            else:
                return True
        return False
