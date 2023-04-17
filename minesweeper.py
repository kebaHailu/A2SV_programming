class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:


        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board


        directions = [(-1,0),(0,-1),(1,-1),(-1,1),(-1,-1),(1,1),(1,0),(0,1)]
        pos = {'E','B','X','M'}
        def inbound(row,col):
            
            return  0<=row<len(board) and 0<= col<len(board[0])
                
            
            
        



        

        def dfs(visited,row,col):

            visited.add((row,col))
            
            
            temp = []
            val = []
            for x , y in directions:
                new_row = x + row 
                new_col = y + col 
                if (new_row,new_col) not in visited and inbound(new_row,new_col): 
                    temp.append((new_row,new_col))
                    val.append(board[new_row][new_col])

            if 'M' in val:
                board[row][col] = str(val.count('M'))
                return 
            for i,j in temp:
                if board[i][j] == 'E':
                    dfs(visited,i,j)

            board[row][col] = 'B' 
        dfs(set(),click[0],click[1])
        return board