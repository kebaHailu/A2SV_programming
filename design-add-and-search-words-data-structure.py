class WordDictionary:

    def __init__(self):
        self.child = {}
        self.isEOW = False
        

    def addWord(self, word: str) -> None:
        curr = self
        for ch in word:
            if curr.child.get(ch) is None:
                curr.child[ch] = WordDictionary()
            curr = curr.child[ch]
        
        curr.isEOW = True 

        

    def search(self, word: str) -> bool:
        curr = self 
        for i in range(len(word)):
            ch = word[i]
            if ch == ".":
                for char  in curr.child.values():
                    if char.search(word[i+1:]):
                        return True 
                return False 
            if curr.child.get(ch) is None:
                return False 
            curr = curr.child[ch]
        return curr and curr.isEOW

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)