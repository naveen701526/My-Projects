class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        r = ''
        for i in range(0, len(s), k*2):
            r += s[i:i+k][::-1] + s[i+k:i+k+k]
        return r
        
opt = Solution()
print(opt.reverseStr('abcdefg', 2))
