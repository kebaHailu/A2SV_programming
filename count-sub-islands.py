class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
    
        def inbound(row,col):
            return 0<= row < len(grid1) and 0<= col < len(grid1[0])

        

        def dfs(islands,row,col):
            # base case 
            if grid2[row][col] == 0:
                return set()
            
            islands.add((row,col))
            grid2[row][col] = 0

            for x,y in directions:
                new_row = row + x 
                new_col = col + y 

                if inbound(new_row,new_col) :
                    dfs(islands,new_row,new_col)
            
            return islands
        possible = []
        for i in range(len(grid1)):
            for j in range(len(grid1[0])):
                island = dfs(set(),i,j)
                if len(island) ==0:
                    continue 
                possible.append(island)

        count = 0
        for pos in possible:
            if all([grid1[x][y]==1 for x,y in pos]):
                count += 1
        return count