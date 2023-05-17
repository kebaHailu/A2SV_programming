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
        repx = self.find(x)
        repy = self.find(y)

        if repx != repy:
            if self.size[repx] > self.size[repy]:
                self.rep[repy] = self.rep[repx]
                self.size[repx] += self.size[repy]
            else:
                self.rep[repx] = self.rep[repy]
                self.size[repy] += self.size[repx]

    def connected(self,x,y):
        return self.find(x) == self.find(y)


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        unions = UnionFind(len(edges))
        for a , b in edges:
            if unions.connected(a-1,b-1):
                return [a,b]
            unions.union(a-1,b-1)