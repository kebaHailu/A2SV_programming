class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = defaultdict(list)

        for i in range(len(s)):
            d[s[i]].append(i)
        
        ans = 0
        for word in words:
            idx = -1
            take = True
            for ch in word:
                    new_idx = bisect_left(d[ch],idx)
                    
                    while new_idx < len(d[ch]) and d[ch][new_idx] <= idx:
                        new_idx += 1 
                    
                    if new_idx == len(d[ch]):
                        take = False
                        break
                    idx = d[ch][new_idx]
            
            if take:
                ans += 1
           

        
        return ans