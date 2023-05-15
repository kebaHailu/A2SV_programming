from collections import deque
from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
	
		visited = set()
		queue = deque()
		for i in range(V):
		    if i not in visited:
		        queue.append((i , -1))
		        visited.add(i)
		    while queue:
		        node , parent = queue.popleft()
		        for child in adj[node]:
		            if child in visited and child != parent:
		                return True
		            elif child not in visited:
		                queue.append((child , node))
                        visited.add(child)
                        
        return False
		    


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends