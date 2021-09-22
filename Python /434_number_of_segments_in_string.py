class Solution:
    def countSegments(self, s: str) -> int:
        h=0
        c=0
        # s=' '+s
        if not s:
            return 0
        for i in range(len(s)):
            if(s[i]!=' '):
                h+=1
            elif(h>0): 
                c+=1
                h=0
        if(h>0):
            c+=1
        return c
        
        
opt = Solution()
print(opt.countSegments('Hello, my name is John'))
