class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        direction = [(0,1),(1,0),(-1,0),(0,-1)]
        def inbound(row,col):
            return 0<=row<n and 0<=col<m
        

        visited = set()
        queue = deque()
        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    queue.append((i,j))
                    visited.add((i,j))

        while queue:
            length = len(queue)

            for _ in range(length):
                x , y = queue.popleft()

                for i,j in direction:
                    xi = x+i
                    yj = y+j

                    if inbound(xi,yj) and (xi,yj) not in visited:
                        mat[xi][yj] = mat[x][y] + 1 
                        queue.append((xi,yj))
                        visited.add((xi,yj))
        
        return mat