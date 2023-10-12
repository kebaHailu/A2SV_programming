class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        def hashToInt(word):
            y = 0
            for idx,ch in enumerate(word):
                y += (ord(ch)-96) * 26 ** ( len(word)-idx-1)
                
            return y
        
        needleVal = hashToInt(needle)
        print(haystack[:len(needle)])
        x = hashToInt(haystack[:len(needle)])
        if x == needleVal:
            return 0
       
        for i in range(len(haystack)-len(needle)):
            x -= (ord(haystack[i])-96) * (26** (len(needle)-1))
            x *= 26
            x += ord(haystack[i+len(needle)]) - 96
            

            if x == needleVal:
                return i+1 
        return -1