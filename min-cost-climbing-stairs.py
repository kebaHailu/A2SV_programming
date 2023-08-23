class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mincost = cost + [0]

        for i in range(2,len(mincost)):
            mincost[i] = min(mincost[i-1],mincost[i-2])+mincost[i]
        
        
        return mincost[-1]