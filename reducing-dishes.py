class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort() 

        prefix = 0 
        tot = 0 

        for i in range(len(satisfaction)-1,-1,-1):
            prefix += satisfaction[i]

            if prefix >= 0:
                tot += prefix 
        
        return tot