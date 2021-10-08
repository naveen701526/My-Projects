class MyStack:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        a = self.queue.pop()
        return a

    def top(self) -> int:
        a = self.queue[-1]
        return a

    def empty(self) -> bool:
        if self.queue:
            return False
        else:
            return True
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
param_2 = obj.pop()
print(obj.queue)
param_3 = obj.top()
print(param_3)

param_4 = obj.empty()
print(param_4)
