class UnionFind:
    def __init__(self,size):

        self.rep = [i for i in range(size)]
        self.size = [1]*size
    def find(self,x):
        if x == self.rep[x]:
            return x 
        self.rep[x] = self.find(self.rep[x])
        return self.rep[x]
    def union(self,x,y):
        xrep = self.find(x)
        yrep = self.find(y)

        if xrep != yrep:
            if self.size[xrep] > self.size[yrep]:
                self.size[xrep] += self.size[yrep]
                self.rep[yrep] = self.rep[xrep]
                
            else:
                self.rep[xrep] = self.rep[yrep]
                self.size[yrep] += self.size[xrep]
    def connected(self,x,y):
        print(self.rep)
        return self.find(x) == self.find(y)
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        unions = UnionFind(n)
        for a,b in edges:
            unions.union(a,b)
        

        return unions.connected(source,destination)