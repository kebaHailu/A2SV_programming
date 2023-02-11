class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        i1 = 0
        i2 = 0
        
        
        merge = ""
        while i1 < len(word1) and i2 < len(word2):
            
            if word1[i1:] > word2[i2:]:
                merge += word1[i1]
                i1 += 1
         
            else :
                merge += word2[i2]
                i2 += 1
        merge += word1[i1:]
        merge += word2[i2:]
        
        return merge
    
                