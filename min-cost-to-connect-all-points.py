class UnionFind:
    def __init__(self,points):
        self.rep = {tuple(i):tuple(i) for i in points}
    def find(self,x):
        if x != self.rep[x]:
            self.rep[x] = self.find(self.rep[x])
        return self.rep[x]
    def union(self,x,y):
        xrep = self.find(x)
        yrep = self.find(y)

        if xrep != yrep:
            self.rep[xrep] = yrep 
            return True 
        return False 


class Solution:
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        arr = []
        unions = UnionFind(points)
        n = len(points)
        for i in range(n):
            for j in range(i+1,n):
                
                mht = self.manhattan(points[i],points[j])
                temp = [mht,points[i],points[j]]
                arr.append(temp)
        arr.sort()
        ans = 0
        for d,a,b in arr:
            a = tuple(a)
            b = tuple(b)
            if unions.union(a,b):
                ans += d 
            

        return ans



        
    











    def manhattan(self,a,b):
        ai,aj = a
        bi,bj = b
        
        return abs(ai-bi)+abs(aj-bj)