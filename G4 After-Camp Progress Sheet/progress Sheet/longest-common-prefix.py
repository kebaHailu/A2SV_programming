class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.endOfWord = True
    
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.endOfWord

    def allstartsWith(self, node):
        curr = self.root

        ans = ""
        while len(curr.children) == 1 and not curr.endOfWord:
            
            for i in curr.children.keys():
                ans += i if i != '*' else ""
                curr = curr.children[i]

        return ans

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        t = Trie()
        for s in strs:
            if s == "":
                t.insert("*")
            t.insert(s)

        return t.allstartsWith(t.root)