class ThroneInheritance:

    def __init__(self, kingName: str):
        self.name = kingName 
        self.throne = {kingName:[]}
        self.dead = set()
        

    def birth(self, parentName: str, childName: str) -> None:
        if parentName in self.throne:
            self.throne[parentName].append(childName)
        else:
            self.throne[parentName] = [childName]
        

    def death(self, name: str) -> None:
        self.dead.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        order = []
        def dfs(successor=self.name):
            if successor not in self.dead:
                order.append(successor)
            if successor in self.throne:
                for child in self.throne[successor]:
                    dfs(child)

        dfs()
        return order 

            
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()