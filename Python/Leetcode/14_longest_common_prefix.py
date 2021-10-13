class Solution:
    def longestCommonPrefix(self, strs: [str]) -> str:
        res=""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or strs[0][i] != s[i]:
                    return res
            res+=strs[0][i]
        return res
        
        
opt = Solution()
print(opt.longestCommonPrefix(["flower","flow","fluctuate"]))
