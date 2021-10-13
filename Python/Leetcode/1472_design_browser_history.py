# https://leetcode.com/problems/design-browser-history/
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_index = 0

    def visit(self, url: str) -> None:
        self.current_index += 1
        self.history = self.history[0:self.current_index]
        self.history.append(url)
        

    def back(self, steps: int) -> str:
        self.current_index = max(0, self.current_index - steps)
        return self.history[self.current_index]

    def forward(self, steps: int) -> str:
        self.current_index = min(len(self.history)-1, self.current_index + steps)
        return self.history[self.current_index]
        


# Your BrowserHistory object will be instantiated and called as such:
obj = BrowserHistory("leetcode.com")
obj.visit("google.com")
obj.visit("facebook.com")
obj.visit("twitter.com")
param_2 = obj.back(1)
param_3 = obj.forward(2)

print(param_2)
print(param_3)
