class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        return s == t
        
        
opt = Solution()
print(opt.isAnagram(s = "anagram", t = "nagaram"))
print(opt.isAnagram(s = "rat", t = "car"))
