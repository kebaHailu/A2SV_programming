
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for idx,val in enumerate(manager):
            graph[val].append(idx)
        
        start = graph[-1]

        queue = deque(graph[-1])
        visit = set(graph[-1])

        def dfs(node):
            ans = 0
            for child in graph[node]:
                ans = max(ans, (dfs(child) + informTime[node]))
            return ans 
        
        return dfs(headID)