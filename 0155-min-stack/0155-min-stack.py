class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
    def pop(self) -> None:
        if self.stack:
            self.stack.pop(-1)

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return -1
        
    def getMin(self) -> int:
        if self.stack:
            return min(self.stack)
        else:
            return -1
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()