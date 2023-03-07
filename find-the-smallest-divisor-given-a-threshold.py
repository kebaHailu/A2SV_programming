class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def helper(k):
            sum = 0

            for num in nums:
                sum += ceil(num/k)

            
            
            return sum <= threshold

        
        left = 0
        right = max(nums) * threshold 


        while left + 1 < right:
            mid = left + (right - left)//2

            if helper(mid):
                right = mid
            
            else :
                left = mid 

        return right