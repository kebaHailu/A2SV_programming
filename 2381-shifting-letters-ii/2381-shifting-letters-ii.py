
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        
        s_list = ['a']*len(s)
        prefix = [0]* (len(s)+1)
        
        for shift in shifts:
            
            left,right ,dtn = shift
            if dtn == 1:
                
                prefix[left] += 1 
                prefix[right+1] -= 1 
                
            else :
                prefix[left] -= 1  
                prefix[right+1] += 1
            
              
        for i in range(1,len(prefix)):
            prefix[i] += prefix[i-1]
        
        
        
        for i in range(len(s)):
             s_list[i] = chr(97 + (ord(s[i])-97 + prefix[i])%26)
        
        
        return ''.join(s_list)
        
            