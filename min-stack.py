class MinStack:

    def __init__(self):
        self.stack = []
        self.min_val = float("inf")
        self.min_stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if val <= self.min_val:
            self.min_val = val 
            self.min_stack.append(val)

        

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
            if self.min_stack:
                self.min_val = self.min_stack[-1]
            else:
                self.min_val = float("inf")
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()