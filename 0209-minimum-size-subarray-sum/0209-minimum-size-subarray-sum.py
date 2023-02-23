class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        left = 0
        
        firstsum = 0
        length = float("inf") 
        for right in range(len(nums)):
            firstsum += nums[right]
            while firstsum >= target:
                length =min(length,right - left+1)
                firstsum -= nums[left]
                left += 1 
            
            
             
            
            
            
        return length