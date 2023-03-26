class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            current = nums[i]


            if current >= len(nums):
                continue 
            
            while current != i:
                nums[current],nums[i] = nums[i],nums[current]

                current = nums[i]

                if current >= len(nums):
                    break 
        
        for i in range(len(nums)):
            if nums[i] != i:
                return i
                
        return len(nums)