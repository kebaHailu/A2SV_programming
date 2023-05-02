from collections import defaultdict ,deque

n = int(input())

while n:
    l = int(input())
    graph = defaultdict(list)
    quariy = True 
    
    for _ in range(l):
        a,b = map(int,input().split())
        
        graph[a].append(b)
        graph[b].append(a)
    
    
    colors = [-1]*(n+1)
    
    def bicolor(node,color):
        colors[node] = color 
       
        for child in graph[node]:
            if colors[child] == -1:
               if not bicolor(child,color^1):
                   return False 
            elif colors[child] == color:
                return False 
        return True 
    flag = True 
    for i in range(1,n+1):
        if colors[i] ==-1 and not bicolor(i,0):
            print("NOT BICOLOURABLE.")
            flag = False 
            break
    if flag:
        print("BICOLOURABLE.")
        
            
        
     
        
        
            
                    
            
    
    
        
    
    
    
    
    n = int(input())