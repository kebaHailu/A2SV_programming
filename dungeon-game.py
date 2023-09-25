class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        
        n = len(dungeon)
        m = len(dungeon[0])

        x = dungeon[-1][-1]
        x = 1 - x if 1 - x > 0 else 1
        dungeon[-1][-1] = x
        for i in range(n-2,-1,-1):
            next_move = dungeon[i+1][-1]
            cur_move = dungeon[i][-1]

            needed = next_move - cur_move if next_move - cur_move > 0 else 1
            dungeon[i][-1] = needed 
        
        for i in range(m-2,-1,-1):
            next_move = dungeon[-1][i+1]
            cur_move = dungeon[-1][i]

            needed = next_move - cur_move if next_move - cur_move > 0 else 1
            dungeon[-1][i] = needed 
        
        for i in range(n-2,-1,-1):
            for j in range(m-2,-1,-1):
                x = min(dungeon[i][j+1],dungeon[i+1][j]) - dungeon[i][j]
                x = x if x > 0 else 1 
                dungeon[i][j] = x

        return dungeon[0][0]