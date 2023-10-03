class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        for i in range(len(costs)):
            costs[i].append(costs[i][0]-costs[i][1])
        
        costs.sort(key=lambda x:x[2])
        
        tot = 0
        for idx in range(len(costs)):
            if idx+1 <= len(costs)//2:
                tot += costs[idx][0]
                print(costs[idx])
            else:
                tot += costs[idx][1]
        
        return tot