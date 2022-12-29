
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = Counter(s)
        t_count = Counter(t)
        
        for ch in t_count:
            if ch not in s_count:
                return ch 
            if s_count[ch] != t_count[ch]:
                return ch 