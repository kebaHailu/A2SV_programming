class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 1 and nums[0] == target:
            return [0,0]
        left = 0
        right = len(nums)-1

        ans = [-1,-1]
        # for starting postion
        while left <= right :
            
     
            mid = left + (right - left)//2 

            if target > nums[mid]:
                left = mid + 1 
            else :
                right = mid-1 
        
        if 0 <= left < len(nums) and nums[left] == target:
            ans[0] = left 


        l = 0
        r = len(nums)-1 

        # for ending postion 
        while l <= r:
          
            mid = l + (r - l)//2 
            if target < nums[mid]:
                r = mid -1 
            else :
                l = mid + 1

        if 0 <= r < len(nums) and nums[r] == target:
            ans[1] = r
    
        return ans