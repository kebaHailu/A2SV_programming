class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        count = 0

        while x or y:
            count += (x&1)^(y&1)
            x >>= 1
            y >>= 1
        
        return count