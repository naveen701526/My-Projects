class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans=0
        for x in columnTitle:
            ans=ans*26+ord(x)-ord('A')+1
        return ans
        
        
opt = Solution()
print(opt.titleToNumber('ZY'))
