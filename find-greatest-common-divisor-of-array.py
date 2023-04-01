class Solution:
    def findGCD(self, nums: List[int]) -> int:
        n = max(nums)
        d = min(nums)

        def gcd(n,d):
            # this is the general formula to solve gcd problems 
            if d == 0:
                return n
            
            return gcd(d,n%d)
        
        return gcd(n,d)