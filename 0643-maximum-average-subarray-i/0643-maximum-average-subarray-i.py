class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        max_sum = sum(nums[:k])
        max_avg = max_sum / k 
        
        i = 0
        j = k 
        
        
        new_avg = max_avg
        while j < len(nums):
            
            new_avg = new_avg - nums[i]/k + nums[j]/k 
            
            max_avg = max(max_avg,new_avg)
            
            i += 1
            j += 1
        
        return max_avg
            
            