class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        def bfs():
            queue = deque()
            visited = set()
            visited.add(0)
            queue.append(0)
            
            while queue:
                    
                    
                node = queue.popleft()

                for i in rooms[node]:
                    if i not in visited:
                        queue.append(i)
                        visited.add(i)
            
            
            return len(visited)

        

        length = bfs()

        return length == len(rooms)