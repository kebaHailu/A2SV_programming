class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = [0] * (len(nums))
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                
                if i != j and nums[i] > nums[j]:
                    arr[i] += 1
        return arr