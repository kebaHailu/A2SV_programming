class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        visited = set()
        possible_path = set()
        def inbound(row,col):
            return 0<=row<n and 0<=col<m 
        

        def bfs(row,col):
            queue = deque([(row,col)])
            visited.add((row,col))

            while queue:
                level_wise = len(queue)
                for _ in range(level_wise):
                    x,y = queue.popleft()

                    for i,j in direction:
                        xi = x+i
                        yj = y+j 

                        if inbound(xi,yj) and (xi,yj) not in visited and grid[xi][yj] == 1:
                            queue.append((xi,yj))
                            visited.add((xi,yj))
        
        def findpath():
            queue = deque()
            for x in visited:
                queue.append(x)
                possible_path.add(x)
            count = 0
            
            while queue:
                level_wise = len(queue)
                count += 1
                for _ in range(level_wise):
                    row,col = queue.popleft()
                    for i,j in direction:
                        new_row = row + i 
                        new_col = col + j 
                        if inbound(new_row,new_col) and (new_row,new_col) not in possible_path:
                            if grid[new_row][new_col] == 1:
                                return count-1
                            queue.append((new_row,new_col))
                            possible_path.add((new_row,new_col))
                
                
            
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    bfs(i,j)
                    print(visited)
                    return findpath()