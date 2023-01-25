class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        arr = [list(col[::-1]) for col in zip(*matrix)]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = arr[i][j]




