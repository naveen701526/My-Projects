class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        
        return -1
        
opt = Solution()
print(opt.strStr('hello', 'll'))
