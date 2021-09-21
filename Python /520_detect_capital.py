class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if len(word) < 2:
            return True
        
        lower = upper = 0
        
        for letter in word:
            if letter.isupper(): upper += 1
            else: lower += 1
        
        if (upper == 0) or (lower == 0) or (upper == 1 and word[0].isupper()):
            return True
        return False
        
opt = Solution()
print(opt.detectCapitalUse('USA'))
