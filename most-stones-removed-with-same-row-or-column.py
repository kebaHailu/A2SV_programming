class UnionFind:
    def __init__(self,s):
        self.rep = {tuple(i):tuple(i) for i in s}
        self.size = {tuple(i):1 for i in s}
        
    def find(self,x):
        if x == self.rep[x]:
            return x
        self.rep[x] = self.find(self.rep[x])
        return self.rep[x]
    
    def ans(self):
        val = 0
        visited = set()
        for k,i in self.size.items():
            parent = self.find(k)
            if parent not in visited:
                val += self.size[parent] - 1
                visited.add(parent)
        print(self.size)
        return val
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
    def removeStones(self, stones: List[List[int]]) -> int:
        unions = UnionFind(stones)
        n = len(stones)
        for i in range(n):
            for j in range(i+1,n):
                a,b = stones[i]
                x,y = stones[j]
                if a == x or b == y:
                    unions.union((a,b),(x,y))
        
        return unions.ans()