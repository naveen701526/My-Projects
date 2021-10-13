class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()', 'o').replace('(al)', 'al')
        
        
string = Solution()
print(string.interpret('G()(al)'))
