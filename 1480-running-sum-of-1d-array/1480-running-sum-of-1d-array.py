class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix_sum = []
        cur_sum = 0
        for num in nums:
            cur_sum += num
            
            prefix_sum.append(cur_sum)
            
        
        
        return prefix_sum
            
            