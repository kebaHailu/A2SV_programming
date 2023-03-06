for _ in range(int(input())):
    n , m = map(int,input().split())
    
    ans = (n+m)//4
    print(min(ans,n,m))