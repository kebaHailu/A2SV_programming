class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window = defaultdict(int)
        
        max_length = 0
        
        left = 0
      
        
        for right in range(len(fruits)):
            
            window[fruits[right]] += 1
            
            while len(window) > 2:
                window[fruits[left]] -= 1 
                
                if window[fruits[left]] == 0:
                    del window[fruits[left]]
                
                left += 1 
                
            
            max_length = max(max_length , right - left + 1)
            
           
        
        return max_length
    
            
            
        
                
                
            