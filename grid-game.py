class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        prifix1 = [0] * (len(grid[0]) + 1)
        prifix2 = [0] * (len(grid[0]) + 1)
       

        for i in range(len(grid[0])):
            prifix1[i+1] = prifix1[i]+ grid[0][i]
            prifix2[i+1] = prifix2[i]+ grid[1][i]
        


        ans = float("inf")
        for i in range(1,len(prifix1)):

            upper = prifix1[-1] - prifix1[i]
            lower = prifix2[i-1]
            
            ans = min(ans,max(upper,lower))

        return ans