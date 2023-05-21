class UnionFind:
    def __init__(self):
        self.rep = {i:i for i in ascii_lowercase}
    
    def find(self,x):
        if self.rep[x] == x:
            return x 
        self.rep[x] = self.find(self.rep[x])
        return self.rep[x]
    
    def union(self,x,y):
        xrep = self.find(x)
        yrep = self.find(y)
        if xrep != yrep:
            self.rep[xrep] = yrep
    def connected(self,x,y):
        return self.find(x) == self.find(y)
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        unlike = []
        unions = UnionFind()
        for equ in equations:
            a,b,c,d = equ 
           
            if b == "=":
                unions.union(a,d)
            else:
                unlike.append((a,d))
        
        for x,y in unlike:
            if unions.connected(x,y):
                return False 
        
        return True