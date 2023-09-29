class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = 0 
        self.value = 0
class MapSum:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, key: str, val: int) -> None:
        node = self.root 
        for ch in key:
            if ch not in node.children:
                node.children[ch] = TrieNode() 
                
            node = node.children[ch]
            node.value += val
        

        if node.endOfWord:
            
            cur_val = node.endOfWord
            node = self.root 
            for ch in key:
                node = node.children[ch]
                node.value -= cur_val
        node.endOfWord = val
        


        

    def sum(self, prefix: str) -> int:
        node = self.root
        val = 0
        
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
            val = node.value
            
        return val
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)