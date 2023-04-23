from sys import stdin,stdout
from collections import Counter,defaultdict 



def I(): return int(stdin.readline())
def II(): return map(int, stdin.readline().split())
def IL(): return list(map(int, stdin.readline().split()))
def SIL(): return sorted(map(int, stdin.readline().split()))



def solve():
    
    # write your code here 
    n,m = II()
    
    
    
    
    def gcd(a,b):
        if b == 0:
            return a 
        return gcd(b,a%b)
    
    temp = gcd(n,m)
    for i in range(n,m):
        temp = gcd(temp,i)
        if temp == 1:
            return 1 
    return temp 
   
        
    
    
    
    
    
    
    



print(solve())
