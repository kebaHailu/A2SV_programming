class UnionFind:
    def __init__(self,size):
        self.rep = [i for i in range(size)]
        self.size = [1]*size
        self.wight = [10**4]*size
        

    def find(self,x):
        if x == self.rep[x]:
            return x 
        self.rep[x] = self.find(self.rep[x])
        return self.rep[x]
    def mindis(self,x):
        print(self.wight)
        return self.wight[self.find(x)]

    def union(self,x,y,w):
        repx = self.find(x)
        repy = self.find(y)
        minwight = min(w,self.wight[repx],self.wight[repy])


        if repx != repy:
            if self.size[repx] > self.size[repy]:
                self.rep[repy] = self.rep[repx]
                
                self.size[repx] += self.size[repy]
            else:
                self.rep[repx] = self.rep[repy]
                
                self.size[repy] += self.size[repx]
        
        self.wight[repx] = minwight
        self.wight[repy] = minwight


    def connected(self,x,y):
        return self.find(x) == self.find(y)


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        unions = UnionFind(n)
        for a,b,w in roads:
            unions.union(a-1,b-1,w)
        
        return unions.mindis(n-1)