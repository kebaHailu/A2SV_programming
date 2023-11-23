class Solution(object):
    def moveZeroes(self, nums):
        
        holder=0
        for seeker in range(len(nums)):
            if(nums[seeker]!=0):
                nums[holder],nums[seeker]=nums[seeker],nums[holder]
                holder +=1
        return(nums)