class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        min_sum = 0
        dty = {}
        dty[0] = 1
        
        for i in range(len(nums)):
            
            min_sum += nums[i] 
            count += dty.get(min_sum-k,0)
            dty[min_sum] = dty.get(min_sum,0)+1
            
        return count 