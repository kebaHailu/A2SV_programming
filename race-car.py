class Solution:
    def racecar(self, target: int) -> int:

        def A(node):
            a , b = node
            return (a+b, b*2)
        def R(node):
            a,b = node
            if b > 0:
                b = -1
            else:
                b = 1
            return (a,b)

        visited = set([(0,1)])
        queue = deque()
        queue.append((0,1))
        count = 0

        while queue:
            count += 1
            length = len(queue)
            for _ in range(length):

                node = queue.popleft()

                left = A(node)
                if left not in visited:
                    a , b = left 
                    if a == target:
                        return count 
                    visited.add(left)
                    queue.append(left)


                right = R(node)
                if right not in visited:
                    x , y = right
                    if x == target:
                        return count
                    visited.add(right)
                    queue.append(right)