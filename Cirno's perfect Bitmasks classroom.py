from sys import stdin,stdout
from collections import Counter,defaultdict 

def I(): return int(stdin.readline())
def II(): return map(int, stdin.readline().split())
def IL(): return list(map(int, stdin.readline().split()))
def SIL(): return sorted(map(int, stdin.readline().split()))



def solve():
    
    # write your code here 
    x = I()
    r = x
    y = 1
    
    def ones(r):
        countone = 0
        while r:
            countone += (r&1)
            r >>= 1 
        
        return countone 
    
        
    
    
    while x:
        if (x&1):
            break 
        x >>= 1 
        y <<= 1 
 
    if ones(r) > 1:
        
        return y
    while ones(y) <= 1:
        
        y += 1
    
    return y
    
    
    
    
    
    
    
    
    


for _ in range(I()):
    print(solve())
