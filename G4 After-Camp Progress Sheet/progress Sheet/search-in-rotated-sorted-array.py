class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1

        while left < right:
            mid = (left + right)//2 
            if nums[mid] > nums[right]:
                left = mid + 1 
            else:
                right = mid 


        rotate = left 
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = (left + right)//2 
            realmid = (mid + rotate)%len(nums)
            if nums[realmid] == target:
                return realmid
            if (nums[realmid] < target):
                left = mid + 1 
            else:
                right = mid -1 
        
        return -1

        