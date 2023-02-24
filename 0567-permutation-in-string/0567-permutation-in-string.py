class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_counter = Counter(s1)
        s2_counter = Counter()
        
        window = len(s1)
        
        for idx , ch in enumerate(s2):
            
            s2_counter[ch] += 1 
            
            if idx >= window:
                s2_counter[s2[idx-window]] -= 1 
            
            if s1_counter == s2_counter:
                return True 
            
        return False 
    