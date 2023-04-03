class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_val = min(nums)
        nums = set(nums)
       

        for i in range(1,2**31):
            if i not in nums:
                return i