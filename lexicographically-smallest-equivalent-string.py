class UnionFind:
    def __init__(self,s):
        self.rep = {i:i for i in s}
    
    def find(self,x):
        if x not in self.rep:
            return x 
            
        if self.rep[x] == x:
            return x 
        self.rep[x] = self.find(self.rep[x])
        return self.rep[x]
    
    def union(self,x,y):
        xrep = self.find(x)
        yrep = self.find(y)
        if xrep > yrep:
            self.rep[xrep] = yrep
        else:
            self.rep[yrep] = xrep 
        




class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        unions = UnionFind(s1+s2)
        for i in range(len(s1)):
            unions.union(s1[i],s2[i])
        ans = ""
        for i in baseStr:
            ans += unions.find(i)
        
        return ans