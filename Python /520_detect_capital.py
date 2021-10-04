class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if len(word) < 2: #if word is single letter or no letter 
            return True
        
        lower = upper = 0 #counts the number of lowercase and uppercase letters
        
        for letter in word:
            if letter.isupper(): upper += 1 #count the uppercase in string
            else: lower += 1 #count the lowercase in string
        
        #checks if uppercase letter are zero or lowercase letters in string are zero 
        #or Start letter is uppercase in string
        if (upper == 0) or (lower == 0) or (upper == 1 and word[0].isupper()):
            return True
        return False
        
opt = Solution()
print(opt.detectCapitalUse('USA'))

