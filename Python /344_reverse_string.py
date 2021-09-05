class Solution:
    def reverse(self, s, i):
        if len(s) - 1 - i <= i:
            return s
        
        s[i],s[len(s) - 1 - i] = s[len(s) - 1 - i], s[i]
        return self.reverse(s,i+1)
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        return self.reverse(s,0)
    
opt = Solution()
print(opt.reverseString(['h','e','l','l','o']))
