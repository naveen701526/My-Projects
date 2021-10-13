class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        reverseIndex = len(s) - 1
        while reverseIndex >= 0:
            if s[reverseIndex] == ' ':
                if length > 0:
                    return length
            else:
                length += 1
            reverseIndex -= 1
        return length
        
opt = Solution()
print(opt.lengthOfLastWord('Hello World'))
