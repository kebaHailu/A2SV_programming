class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        end = len(piles)-1
        add_to_three = 0
        for i in range(len(piles)//3):
            add_to_three += piles[end-(i*2)-1]
            
        
        return add_to_three
            
        
        