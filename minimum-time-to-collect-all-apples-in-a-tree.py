class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        
        graph = defaultdict(list)

        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            

        
        def dfs(node,visited,count):
           
            
            visited.add(node)
            time = 0
            for nb in graph[node]:
                if nb not in visited:
                    val = dfs(nb,visited,count+1)
                    if val > count:
                        time += (val-count)
            print(time,count,node)
            if time:
                return time+count+1
            else:
                if hasApple[node]:
                    return count+1
                else:
                    return count-1 
            
                

        ans = dfs(0,set(),0)-1
       
        
        
        return ans if ans > 0 else 0