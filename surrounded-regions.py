class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rl = len(board)
        cl = len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
        def inboarder(row,col):
            return 0<= row < rl and 0<=col<cl 
        
        def onboarder(row,col):
            return row==0 or row ==rl-1 or col == 0 or col ==cl-1 
        
        
        def dfs(row,col):
            if not inboarder(row,col) or board[row][col] != 'O':
                return 
            board[row][col] = 'K'
            for x , y in directions:
                new_row = x + row 
                new_col = y + col 
                dfs(new_row,new_col)
                
        for i in range(rl):
            for j in range(cl):
                if onboarder(i,j):
                    dfs(i,j)
        
        for i in range(rl):
            for j in range(cl):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'K':
                    board[i][j] = 'O'