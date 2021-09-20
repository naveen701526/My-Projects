class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> [str]:
        ans, stack = [], []
        for w in text.split():
            if len(stack) > 1 and stack[-2] == first and stack[-1] == second:
                ans.append(w)
            stack.append(w)
        return ans
        
        
opt = Solution()
print(opt.findOcurrences('alice is a good girl she is a good student','a','good'))
