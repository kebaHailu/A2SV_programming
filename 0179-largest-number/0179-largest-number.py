class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strs = list(map(str,nums))
        
        for _ in range(len(strs)):
            
            for i in range(len(strs)-1):
                if  strs[i] + strs[i+1] < strs[i+1] + strs[i]:
                    strs[i],strs[i+1] = strs[i+1],strs[i]



                
        
        
        
                    
                    
            
            
                    
            
            
            
            

            
        
        return str(int(''.join(strs)))