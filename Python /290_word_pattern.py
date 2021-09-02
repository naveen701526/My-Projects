class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        mapped = {}
        used = {}
        if len(pattern) != len(words):
            return False
        for i,char in enumerate(pattern):
            if char not in mapped:
                if used.get(words[i]):
                    return False
                else:
                    mapped[char] = words[i]
            else:
                if mapped.get(char) != words[i]:
                    return False
            used[words[i]] = True
        return True
                    
        
            
opt = Solution()
print(opt.wordPattern('abba', 'dog cat cat dog'))
print(opt.wordPattern('abba', 'dog cat cat fish'))
