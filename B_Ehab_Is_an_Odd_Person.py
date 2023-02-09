n = int(input())
arr = list(map(int,input().split()))

i = 0
even = False 
odd = False 

while i < n:
    
    if arr[i] % 2 == 0:
        
        even = True 
    else :
        odd = True 
        
    i += 1 

if even and odd:
    arr.sort()
print(*arr)