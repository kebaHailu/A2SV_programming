class Solution:
    def balancedString(self, s: str) -> int:
        
        minLength = len(s)
        
        counter = Counter(s)

        n = int(len(s)/4) 
        extra = {}
        for c in counter: 
            if counter[c] > n: extra[c] = counter[c] - n
        if not extra: return 0
        distincts = len(extra)
        i,j = 0,0
        while j < len(s):
            if s[j] in extra: 
                extra[s[j]] -= 1
                if extra [s[j]] == 0: distincts -= 1
            
            while distincts == 0:
                minLength = min(minLength, j - i + 1)
                if s[i] in extra:
                    extra[s[i]] += 1
                    if extra [s[i]] == 1: distincts += 1 
                i += 1
            
            j += 1       
        
        return minLength