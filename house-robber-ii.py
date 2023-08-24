class Solution:
    def calculate(self, nums):
        if len(nums) < 3:
            return max(nums)
        for i in range(len(nums)-3,-1,-1):
            nums[i] += max(nums[i+2:])

        return max(nums)

    def rob(self, nums: List[int]) -> int:       
        if len(nums) == 1:
            return nums[0] 
        return max(self.calculate(nums[:-1]),self.calculate(nums[1:]))