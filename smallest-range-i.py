class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        
        return max(nums) - min(nums) - 2*k if max(nums)-min(nums)-2*k >= 0 else 0