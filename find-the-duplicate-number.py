class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        n = len(nums)

        i = 0


        while i < n:
            
            cp = nums[i] # correct position

            while  cp != i + 1:
                if nums[cp-1] == nums[i]:
                    return nums[i]
                nums[cp-1],nums[i] = nums[i],nums[cp-1]
                cp = nums[i]
            i += 1