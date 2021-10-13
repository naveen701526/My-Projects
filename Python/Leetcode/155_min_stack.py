class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        
        minval = val if not self.minstack else min(val, self.minstack[-1])
        self.minstack.append(minval)
        
    def pop(self) -> None:
        self.stack.pop();
        self.minstack.pop()
             
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2)
obj.push(-2)
obj.push(3)
obj.push(1)
print(obj.pop())
param_3 = obj.top()
param_4 = obj.getMin()

print(param_3)
print(param_4)
