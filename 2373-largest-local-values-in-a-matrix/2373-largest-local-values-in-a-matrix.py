class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:

        x = len(grid)
        arr = [[0]*(x-2) for _ in range(x-2)]

        for i in range(x-2):
            for j in range(x-2):
                arr[i][j] = max([grid[m][n] for m in range(i,i+3) for n in range(j,j+3)])
        
        return arr