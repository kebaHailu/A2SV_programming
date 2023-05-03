class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1*s for s in stones]

        heapify(stones)

        while len(stones) > 1:
            val1 = heappop(stones)
            val2 = heappop(stones)

            if val1 == val2:
                pass 
            else:
                heappush(stones,val1-val2) # -8-(-7) = -1 
        
        if stones:
            return -1*heappop(stones)
        return 0