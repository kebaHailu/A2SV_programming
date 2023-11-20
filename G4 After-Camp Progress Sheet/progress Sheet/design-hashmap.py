class KeyNode:
    def __init__(self,key=-1,val=None):
        self.key = key
        self.val = val
        self.next = None 
        
class MyHashMap:

    def __init__(self):
        self.hashmap = [ KeyNode() for _ in range(40009)]
        self.capacity = len(self.hashmap)

    def hash(self,key):
        return key % self.capacity

        

    def put(self, key: int, value: int) -> None:
        index = self.hash(key)
        cur = self.hashmap[index]

        while cur.next:
            if cur.next.key == key:
                cur.next.val = value
                return 
            cur = cur.next 

        cur.next = KeyNode(key,value)
        

    def get(self, key: int) -> int:
        index = self.hash(key)
        cur = self.hashmap[index]

        while cur:
            if cur.key == key:
                return cur.val 
            cur = cur.next
        
        return -1 

        

    def remove(self, key: int) -> None:
        index = self.hash(key)
        cur = self.hashmap[index]
        if cur.key == key:
            cur = cur.next 
            return 

        while cur and cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next 
                return 
            cur = cur.next 
        
            
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)