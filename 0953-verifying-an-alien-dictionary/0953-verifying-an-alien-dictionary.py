class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic={}
        wordlist =[]
        
        for ind,val in enumerate(order):
            dic[val] = ind 
        
        for word in words:
            newlist =[]
            
            for ch in word:
                newlist.append(dic[ch])
                
            wordlist.append(newlist)
            
        for w1 , w2 in zip(wordlist,wordlist[1:]):
            if w1 > w2 :
                return False 
            
        return True 