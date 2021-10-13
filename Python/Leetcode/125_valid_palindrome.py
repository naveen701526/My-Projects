class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1=list(s)
        input=[]
   
        for i in range(len(s1)):
            if s1[i].isalnum()==True:
                input.append(s[i].lower())
    
        return input==input[::-1]
        
opt = Solution()
print(opt.isPalindrome('A man, a plan, a canal: Panama'))
