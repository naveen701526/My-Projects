class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        s = s+s
        return s.find(goal) != -1
        
opt = Solution()
print(opt.rotateString(s = "abcde", goal = "cdeab"))
