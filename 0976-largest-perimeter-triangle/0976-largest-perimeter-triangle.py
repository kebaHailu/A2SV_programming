class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        # fist return if the length of nums is less than three
        if len(nums) < 3:
            return 0 
        nums.sort()
        # declear three sides 
        i = 0
        j = 1
        k = 2
        p = 0 
        
        while len(nums) > k :
            
            
            if nums[i] + nums[j] > nums[k]:               
                p = max(p, nums[i]+nums[j]+nums[k])
            
            i += 1
            j += 1
            k += 1
            
        return p