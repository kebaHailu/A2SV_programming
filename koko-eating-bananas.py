class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def check(k):
            
            psum = 0
            for i in piles:
                psum += ceil(i/k)
            return psum <= h

        
        left = 0
        right = max(piles)

        while left + 1 < right:
            mid = left + (right - left)//2 

            if check(mid):
                right = mid
            else :
                left = mid
            
        return right