class Solution:
    def union(self,x,y):
        self.rep[self.find(x)] = self.find(y)
    def find(self,x):
        if self.rep[x] == x:
            return x 
        self.rep[x] = self.find(self.rep[x])
        return self.rep[x]
    
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        self.rep = list(range(len(s)))
        for a,b in pairs:
            self.union(a,b)
        

        group = defaultdict(lambda: ([],[]))
        for idx,chr in enumerate(s):
            parent = self.find(idx)
            group[parent][0].append(idx)
            group[parent][1].append(chr)
        
        res =['']*len(s)
        for idx,chars in group.values():
            idx.sort()
            chars.sort()
            for ch,i in zip(chars,idx):
                res[i] = ch
        
        return ''.join(res)