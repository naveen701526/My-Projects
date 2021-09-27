class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c=0
        g=0
        x=''
        for i in s:
            if(c==0):
                g+=1
                x=i
                c+=1
            elif(i==x):
                c+=1
            else:
                c-=1
        return g
        
opt = Solution()
print(opt.balancedStringSplit(s = "RLRRLLRLRL"))
