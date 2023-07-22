class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # the idea is first we take the number as a minimum as possible 
        # then take the second number minimum and finally we will find 
        # the last number to be varify our answer 

        prev = float("inf")
        next = float("inf")

        for val in nums:
            if val <= prev:
                prev = val 
            elif val <= next:
                next = val 
            else :
                # finally we find the the third number 
                return True 
        
        return False