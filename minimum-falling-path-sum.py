class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        def addmin(row,col):
            val = matrix[row][col]
            if row-1>-1:
                y = float("inf")
                z = float("inf")
                x = matrix[row-1][col]
                if col-1>-1:
                    y = matrix[row-1][col-1]
                if col+1<len(matrix[0]):
                    z = matrix[row-1][col+1]
                val += min(x,y,z)

                matrix[row][col] = val 
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                addmin(i,j)
        
        return min(matrix[-1])