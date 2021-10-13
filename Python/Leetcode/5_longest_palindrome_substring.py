class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxleft = 0
        maxright = 0
        i = 0
        while i < len(s):
            # expand left and right while neighbors are equivalent to letter
            left = i
            for j in reversed(range(i)):
                if s[j] == s[i]:
                    left = j
                else:
                    break
            right = i
            for j in range(i, len(s)):
                if s[j] == s[i]:
                    right = j
                else:
                    break
            
            # no need to examine strings of the same char multiple times
            i = right + 1
            
            # print(f'same char left: {left}, right: {right}')
            # then expand left and right as those letters are equivalent
            while left > 0 and right < len(s) - 1 and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1
            if right - left > maxright - maxleft:
                maxleft = left
                maxright = right
        return s[maxleft:maxright+1]
        
        

opt = Solution()
print(opt.longestPalindrome(s = "babad"))
print(opt.longestPalindrome(s = "cbbd"))
print(opt.longestPalindrome(s = "a"))
print(opt.longestPalindrome(s = "ac"))
