class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:

        if target == source:
            return 0
    
        graph = defaultdict(set)
        for idx, val in enumerate(routes):
            for dest in val:
                graph[dest].add(idx)
        visited = {source}
        queue = deque([source])
        
        buses = 0
        
        while queue:
            buses += 1
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                for idx in graph[node]:
                    for stop in routes[idx]:
                        if stop == target:
                            return buses
                        if stop not in visited:
                            visited.add(stop)
                            queue.append(stop)
                    routes[idx] = [] 
        return -1