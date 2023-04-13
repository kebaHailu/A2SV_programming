#2472 -eolymp operation on graph

# Create an undirected graph that supports the next operations:
# AddEdge(u, v) - add to the graph an edge between the vertices (u, v);
# Vertex(u) - print the list of vertices, adjacent with the vertex u.
# There is no loops and multiple edges in the graph.
from collections import defaultdict 


n = int(input())

graph = defaultdict(list)

for _ in range(int(input())):
    arr = list(map(int,input().split()))
    
    if arr[0] == 1:
        graph[arr[1]].append(arr[2])
        graph[arr[2]].append(arr[1])
    
    else:
        print(*graph[arr[1]])