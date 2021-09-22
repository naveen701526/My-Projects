class Solution:
    def checkRecord(self, s: str) -> bool:
        x = s.count('A')
        for i in range (len(s)-2):
            if (s[i]==s[i+1]==s[i+2] == 'L'):
                return False
        if x<2: 
            return True
        return False
        
opt = Solution()
print(opt.checkRecord('PPALLP'))
