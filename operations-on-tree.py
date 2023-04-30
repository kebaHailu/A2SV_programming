class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent 
        self.graph = defaultdict(list)
        self.locked = defaultdict(int)

        for idx,val in enumerate(self.parent):
            self.graph[val].append(idx)
        

    def lock(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False 
        self.locked[num] = user 
        return True 

        

    def unlock(self, num: int, user: int) -> bool:
        if num not in self.locked or self.locked[num] != user:
            return False 
        del self.locked[num]
        return True 

        

    def upgrade(self, num: int, user: int) -> bool:
        def dfs1(num):
            for curr in self.graph[num]:
                if curr in self.locked:
                    return True 
                if dfs1(curr):
                    return True 
            return False 
        def dfs2(num):
            if num in self.locked:
                return True 
            elif num == -1:
                return False 
            else:
                return dfs2(self.parent[num])
        def dfs3(num):
            for curr in self.graph[num]:
                if curr in self.locked:
                    del self.locked[curr]
                dfs3(curr)
        
        if num in self.locked:
            return False 
        elif not dfs1(num):
            return False 
        elif dfs2(self.parent[num]):
            return False 
        else :
            dfs3(num)
            self.locked[num] = user 
            return True 


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)