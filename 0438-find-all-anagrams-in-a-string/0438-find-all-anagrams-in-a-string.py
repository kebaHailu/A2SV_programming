class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
    
        target = Counter(p)
        
        
        arr = []
        
        
        for i in range(len(s)-len(p)+1):
            
            win = s[i:i+len(p)]
            window = Counter(win)
            
            if window == target:
                arr.append(i)
                      
        return arr