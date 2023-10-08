class TrieNode:
    def __init__(self):
        self.kids = {}
        self.prev = {}

class Trie:

    def __init__(self):
        self.root = TrieNode() 

    def insert(self,idx,word):
        n = len(word)
        node = self.root 
        for ch in word:
            if ch not in node.kids:
                node.kids[ch] = TrieNode() 
            node = node.kids[ch]
            for i in range(n-1,-1,-1):
                pre = word[i:]
                node.prev[pre] = idx 
                
    def search(self,pref,suff):
        node = self.root
        for ch in pref:
            if ch not in node.kids:
                return -1
            node = node.kids[ch]
        return node.prev[suff] if suff in node.prev else -1

        
class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie() 
        for i in range(len(words)):
            self.trie.insert(i,words[i])
        
        

    def f(self, pref: str, suff: str) -> int:
        res = self.trie.search(pref,suff)
        return res
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)