from collections import defaultdict

for i in range(int(input())):
    n,m = map(int,input().split())
    chess_board = []
    max_val=0
    upleft = defaultdict(int)
    downright = defaultdict(int)
    for i in range(n):
        chess_board.append(list(map(int,input().split())))
    
    for i in range(n):
        for j in range(m):
            
            w = i-j
            r = i+j
            
            upleft[w] += chess_board[i][j]   
            downright[r] += chess_board[i][j]  
    for i in range(n):
        for j in range(m):
            
            w = i-j
            r = i+j     
            temp = upleft[w] + downright[r] - chess_board[i][j]
            max_val = max(max_val, temp)
    print(max_val)