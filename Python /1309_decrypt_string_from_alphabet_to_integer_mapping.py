class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = ""
        i = len(s)-1 #pointer to end character of string  
        while i>=0:
            if s[i]=="#": #encounter '#' means character > I
                ans = ans + chr(int(s[i-2:i])+96) #add two characters with base 96
                i=i-2 #hence jump two characters in string
            else: 
                ans = ans + chr(int(s[i])+96) #case for adding single digit number 
            i -= 1 
        return ans[::-1]
        
opt = Solution()
print(opt.freqAlphabets(s = "10#11#12"))
