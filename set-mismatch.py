class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n):
            cp = nums[i] - 1 
            
            while cp != i:
                if nums[cp] == nums[i]:
                    ans = [nums[i],i+1]
                    break 
                cp = nums[i]-1
                nums[cp],nums[i] = nums[i],nums[cp]
        return ans