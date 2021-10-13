class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=['a','e','i','o','u','A','E','I','O','U']
        s1=list(s)
        l,r=0,len(s1)-1
        while(l<r):
            while l<r and s1[l] not in vowels:
                l+=1
            while l<r and s1[r] not in vowels:
                r-=1
            s1[l],s1[r]=s1[r],s1[l]
            l+=1
            r-=1
        return "".join(s1)
        
opt = Solution()
print(opt.reverseVowels('hello'))
