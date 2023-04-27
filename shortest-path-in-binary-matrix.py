class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        direction = [(1,0),(0,1),(0,-1),(-1,0),(1,-1),(-1,1),(1,1),(-1,-1)]
        def inbound(row,col):
            return 0<=row<len(grid) and 0<=col<len(grid[0])
        
        if grid[0][0] == 1 :
            return -1
        def bfs():
            queue = deque()
            queue.append((0,0))
            count = 0
            while queue:
                count += 1 
                length = len(queue)
                for _ in range(length):
                    i,j = queue.popleft()

                    if i == len(grid)-1 and j == len(grid[0])-1:
                        return count

                    for x , y in direction:
                        row = x + i 
                        col = y + j 
                        
                        if inbound(row,col):
                            if grid[row][col] == 0:
                                grid[row][col] = 1
                                queue.append((row,col))

            return -1 
        
        return bfs()