class Trie:
    def __init__(self,maxlen):
        self.root = {}
        self.maxlen = len(bin(maxlen))-2
    
    def insert(self,value):
        node = self.root
        val = bin(value)[2:]
        word = '0'*(self.maxlen - len(val)) + val

        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
            
    
    def search(self,value,num):
        node = self.root
        val = bin(value)[2:]
        word = '0'*(self.maxlen - len(val)) + val
        s = ""
        for ch in word:
            chi = "1" if ch == "0" else "0"

            
            if chi not in node:
                node = node[ch]
                s += ch
            else:
                node = node[chi]
                s += chi
        return int(s,2) ^ num


        
        


    
    



class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie(max(nums))
        for val in nums:
            trie.insert(val)
        

        
        ans = 0
        for val in nums:
            ans = max(ans,trie.search(val,val))
        
        return ans