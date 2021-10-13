class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        l=0
        r=len(x)-1
        while l<r:
            if x[l] != x[r]:
                return False
            l+=1
            r-=1
        return True
        
opt = Solution()
print(opt.isPalindrome(121))
