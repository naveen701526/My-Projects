class Solution:
    def balancedStringSplit(self, s: str) -> int:
        c=0 #counts number of same characters
        g=0 #counts number of splits according to problem statement
        x='' #first character from where the split starts
        for i in s:
            if(c==0): #meaning no split has begun yet
                g+=1  #meaning we have found a split
                x=i   #first character of the split
                c+=1  #count of similar character could be either L/R
            elif(i==x): #current character equals previous character then increase the count c
                c+=1
            else:   #when L/R meet their opposite 
                c-=1
        return g #returns the number of splits
        
opt = Solution()
print(opt.balancedStringSplit(s = "RLRRLLRLRL"))
