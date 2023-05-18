class UnionFind:
    def __init__(self,n,m):
        self.rep = defaultdict()
        self.size = {}
        for i in range(n):
            for j in range(m):
                self.rep[(i,j)] = (i,j)
                self.size[(i,j)] = 1 

    def find(self,x):
        if x == self.rep[x]:
            return x
        self.rep[x] = self.find(self.rep[x])
        return self.rep[x]
    def union(self,x,y):
        repx = self.find(x)
        repy = self.find(y)
        
        if repx != repy:
            if self.size[repx] > self.size[repy]:
                self.rep[repy] = self.rep[repx]
                self.size[repx] += self.size[repy]
            else:
                self.rep[repx] = self.rep[repy]
                self.size[repy] += self.size[repx]
            

  

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])

        def inbound(row,col):
            return 0<=row<n and 0<=col<m
        
        direction = {1:[(0,1),(0,-1)],2:[(1,0),(-1,0)],3:[(0,-1),(1,0)],4:[(0,1),(1,0)],5:[(-1,0),(0,-1)],6:[(-1,0),(0,1)]} 
        unions = UnionFind(n,m)
        for i in range(n):
            for j in range(m):

                for x,y in direction[grid[i][j]]:
                    row = i+x
                    col = j+y 
                    if inbound(row,col):
                        for s,r in direction[grid[row][col]]:
                            nrow = s+row
                            ncol = r+col 
                            if (nrow,ncol) == (i,j):
                                unions.union((i,j),(row,col))
        
        return unions.find((0,0)) == unions.find((n-1,m-1))