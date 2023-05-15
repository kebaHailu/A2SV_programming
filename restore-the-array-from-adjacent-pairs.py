class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        zeros = set()
        for a,b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
            if a not in zeros:
                zeros.add(a)
            else :
                zeros.remove(a)
            if b not in zeros:
                zeros.add(b)
            else:
                zeros.remove(b)

        
        visited = set()
        for i in zeros:
            queue = deque([i])
            visited = set([i])
            ans = []
            while queue:
                node = queue.popleft()
                ans.append(node)
                for nb in graph[node]:
                    if nb not in visited:
                        queue.append(nb)
                        visited.add(nb)
            
            return ans

                

            return dfs(i)