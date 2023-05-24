class UnionFind:
    def __init__(self,n):
        self.res = [0]*n
        self.rep = [i for i in range(n)]
        self.rank = [1]*n
        self.sums = [0]*n
    
    def find(self,x):
        if x != self.rep[x]:
            self.rep[x] = self.find(self.rep[x])
        return self.rep[x]

    def union(self,x,y):
        xrep = self.find(x)
        yrep = self.find(y)
        if self.rank[xrep] < self.rank[yrep]:
            xrep , yrep = yrep,xrep
        self.rep[yrep] = xrep 
        self.rank[xrep] += self.rank[yrep]
        self.sums[xrep] += self.sums[yrep]

       

class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:

        n = len(nums)
        unions = UnionFind(n)

        for x in range(n-1,0,-1):
            y = removeQueries[x]
            unions.sums[y] = nums[y]
            if y and unions.sums[y-1]:
                unions.union(y,y-1)
            if y != n - 1 and unions.sums[y+1]:
                unions.union(y,y+1)
            
            unions.res[x-1] = max(unions.res[x],unions.sums[unions.find(y)])
        
        return unions.res