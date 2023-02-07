
    
for _ in range(int(input())):
    
    n = int(input())
    arr = list(map(int,input().split()))
    
    arr.sort()
    
    flag = True
    
    for index in range(n - 1):
        if (arr[index + 1] - arr[index]) <= 1 :
            continue
        flag = False
        break
    
    
    if flag:
        print("YES")
    else:
        print("NO")