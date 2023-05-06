class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [i*-1 for i in piles]

        heapify(piles)
        for _ in range(k):
            val = heappop(piles)
            nval = floor(val/2) 
        
            if nval == 0:
                continue 
            else:
                heappush(piles,nval)

        return -sum(piles)