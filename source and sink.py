
def myans(n,col_wise):
   
    row_wise = list(zip(*col_wise))
    source = []
    sink = []
    for idx in range(len(col_wise)):
        if 1 not in col_wise[idx]:
            sink.append(idx+1)
        if 1 not in row_wise[idx]:
            source.append(idx+1)
    
    print(len(source),*sorted(source))
    print(len(sink),*sorted(sink))
    
    
    
    
    


n = int(input())
arr = []
for _ in range(n):
    row = list(map(int,input().split()))
    arr.append(row)

myans(n,arr)