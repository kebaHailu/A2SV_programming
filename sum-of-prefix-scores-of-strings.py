class TrieNode:
    def __init__(self):
        self.kids = {}
        self.count = 0
        self.end = False 

class Trie:
    def __init__(self):
        self.root = TrieNode() 
    
    def insert(self,word):
        node = self.root 

        for ch in word:
            if ch not in node.kids:
                node.kids[ch] = TrieNode() 
            node.kids[ch].count += 1 
            node = node.kids[ch]
        node.end = True 
    
    def search(self,word):
        node = self.root
        count = 0
        for ch in word:
            if ch not in node.kids:
                break
            count += node.kids[ch].count
            node = node.kids[ch]
        
        return count


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        arr = []
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        for word in words:
            arr.append(trie.search(word))
        
        return arr