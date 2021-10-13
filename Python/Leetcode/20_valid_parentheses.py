class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for bracket in s:
            if bracket in '([{':
                stack.append(bracket)
                continue
            elif bracket in '])}' and len(stack) == 0:
                return False
            elif bracket == ']' and  stack[-1] != '[':
                return False
            elif bracket == ')' and stack[-1] != '(':
                return False
            elif bracket == '}' and stack[-1] != '{':
                return False
            
            stack.pop()
        if len(stack) == 0:
            return True
        else:
            return False
                
                
opt = Solution()
print(opt.isValid('()[]{}'))
