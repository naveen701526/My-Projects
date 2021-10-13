class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d = {}
        for ch in magazine:  # Making d for value count
            if ch not in d:
                d[ch] = 1
            else:
                d[ch] += 1
                
        for ch in ransomNote:  
            if ch not in d:    # if char not in d 
                return False
            else:                 #if char present chech the count and reduce it
                if d[ch] > 1:
                    d[ch] -= 1
                else:              # if char less then 1 and again appear delete it
                    del d[ch]
        return True       
        
opt = Solution()
print(opt.canConstruct('aa','aab'))
