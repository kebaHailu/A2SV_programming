class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)

        if target == "0000":
           return 0
        elif "0000" in deadends:
            return -1

        queue = deque()
        queue.append("0000")
        visited = set()
        deadends.add("0000")
        count = 0
        while queue:
            length = len(queue)
            for _ in range(length):
                val = list(map(int,queue.popleft()))
                for i in range(4):
                    temp = val[i]
                    x = val[i] + 1
                    y = val[i] - 1 
                    if x > 9: x = 0 
                    if y < 0: y = 9 
                    
                    val[i] = x 
                    possible_target = ''.join(map(str,val))
                    if possible_target == target :
                        return count+1
                    elif possible_target not in deadends :
                        queue.append(possible_target)
                        deadends.add(possible_target)
                    
                    val[i] = y
                    possible_target = ''.join(map(str,val))
                    if possible_target == target:
                        print(target)
                        return count+1
                    elif possible_target not in deadends :
                        queue.append(possible_target)
                        deadends.add(possible_target)
                    val[i] = temp
            count +=1
        
        return -1