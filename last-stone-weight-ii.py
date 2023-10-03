class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        dp = {0}

        for i in stones:
            temp = dp.copy()
            for t in dp:
                temp.add(i+t)
            dp.update(temp)
        
        total = sum(stones)
        half = total // 2 
        print(dp, total)
        for i in range(100):
            val = half - i 
            if val in dp:
                return total - 2*val