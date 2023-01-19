class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        numRows, numCols = len(grid), len(grid[0])
        onesRows, onesCols = [0] * numRows, [0] * numCols
        for row in range(numRows):
            for col in range(numCols):
                onesRows[row] += grid[row][col]
                onesCols[col] += grid[row][col]
        for row in range(numRows):
            for col in range(numCols):
                grid[row][col] = 2 * onesRows[row] + 2 * onesCols[col] - numRows - numCols
        return grid