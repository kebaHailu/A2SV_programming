class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        for idx,bomb in enumerate(bombs):
            bomb.append(idx)
        

        def possible(cur_bomb,next_bomb):
            ai,aj,ar,ap= cur_bomb 
            bi,bj,br,bp= next_bomb 

            d = math.sqrt(((ai-bi)**2) + ((aj-bj)**2))
            if d <= ar:
                return True 
            
            return False 


        
        def dfs(bomb,visited):


            visited.add(tuple(bomb))

            for next_bomb in bombs:
                if tuple(next_bomb) not in visited and possible(bomb,next_bomb):
                    dfs(next_bomb,visited)
            
            return visited
        
        max_bombs = 0 

        for bomb in bombs:
            max_bombs = max(max_bombs,len(dfs(bomb,set())))

        return max_bombs