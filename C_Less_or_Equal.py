n,k = map(int,input().split())
array = list(map(int,input().split()))

array.sort()
# where n = 1 and k = 0
if k == 0:
    if array[0] > 1:
        print(1)
    else :
        print(-1)
elif k <= n-1:
    if array[k-1] != array[k]:
        print(array[k-1])
    else:
        print(-1)
else:
     print(array[k-1])