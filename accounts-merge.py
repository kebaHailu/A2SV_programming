class UnionFind:
    def __init__(self,emails):
        self.rep = {i:i for i in emails}
        
    def find(self,x):
        if self.rep[x] != x:
            self.rep[x] = self.find(self.rep[x])
        return self.rep[x]

    def union(self,x,y):
        xrep = self.find(x)
        yrep = self.find(y)

        if xrep != yrep:
            self.rep[xrep] = yrep
    
    def get_group(self, x):
        group = []
        root_x = self.find(x)
        for i in self.rep:
            if self.find(i) == root_x:
                group.append(i)
        return group
            



class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emails = []
        visited = set()
        for account in accounts:
            emails.extend(account[1:])
        unions = UnionFind(emails)

        for account in accounts:
            x = account[1]
            for i in range(1,len(account)):
                unions.union(x,account[i])
        ans = []
        for account in accounts:
            x = account[0]
            y = account[1]
            yrep = unions.find(y)
            if yrep not in visited:
                val = [x]
                val += sorted(unions.get_group(y))
                visited.add(yrep)
                ans.append(val)
        
        return ans