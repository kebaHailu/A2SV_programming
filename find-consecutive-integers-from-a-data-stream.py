class DataStream:

    def __init__(self, value: int, k: int):
        
        self.v = value 
        self.k = k
        self.queue = deque()
        self.dct = defaultdict(int)


        


    def consec(self, num: int) -> bool:
        self.queue.append(num)
        self.dct[num] += 1

        if len(self.queue) < self.k:
            return 
      
        
        
        else:

            keys = list(self.dct.keys())
            ans = len(keys) == 1 and keys[0] == self.v

            first_val = self.queue.popleft()
            self.dct[first_val] -= 1
            if self.dct[first_val] == 0:
                self.dct.pop(first_val)
            return ans

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)