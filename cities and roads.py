# 992 eolymp -cities and roads 
# In the galaxy of "Milky Way" on the planet "Neptune" there are n cities, 
# some of them are connected by roads. Emperor "Maximus" of Galaxy "Milky Way" 
# has decided to make an inventory of roads on the planet "Neptune". 
# But as it turned out he was not good at math, 
# so he asks you to count the number of roads.

graph = []

for _ in range(int(input())):
    graph.append(list(map(int,input().split())))

path = set()
for i in range(len(graph)):
    for j in range(len(graph[0])):
        
        if graph[i][j] == 1 and (j+1,i+1) not in path:
            path.add((i+1,j+1))

print(len(path))
        