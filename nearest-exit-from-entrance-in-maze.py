class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        n = len(maze)
        m = len(maze[0])

        direction = [(1,0),(0,1),(-1,0),(0,-1)]
        def inbound(row,col):
            return 0<=row<n and 0<=col<m 

        a,b = entrance
        visited = set([(a,b)])
        queue = deque([(a,b)])
        count = 0
        
        while queue:
            
            length = len(queue)
            for _ in range(length):
                x,y = queue.popleft()

                for i,j in direction:
                    row , col = x+i,y+j
                    if (row,col) not in visited:
                        if not inbound(row,col):
                            if a != x or b != y:
                                return count if count > 0 else -1
                            
                        elif maze[row][col] == '.':
                            queue.append((row,col))
                            visited.add((row,col))
           
            count += 1
        
        return -1