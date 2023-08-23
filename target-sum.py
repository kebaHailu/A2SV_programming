class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = {}
        def bt(idx,tot):
            if idx == len(nums):
                return 1 if tot == target else 0
            if (idx,tot) in dp:
                return dp[(idx,tot)]
            dp[(idx,tot)] = bt(idx+1,tot-nums[idx]) + bt(idx+1,tot+nums[idx])
            return bt(idx+1,tot-nums[idx]) + bt(idx+1,tot+nums[idx])
            
        return bt(0,0)