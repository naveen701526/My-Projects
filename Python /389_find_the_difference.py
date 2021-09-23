class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # create mapping of string s, which counts the occurences of each letter in s
        mapping_s = {}
        for i in s:
            if i in mapping_s:
                mapping_s[i] = mapping_s[i] + 1
            else:
                mapping_s[i] = 1
        # create mapping of string t, which counts the occurences of each letter in t
        mapping_t = {}
        for i in t:
            if i in mapping_t:
                mapping_t[i] = mapping_t[i] + 1
            else:
                mapping_t[i] = 1
        # create mapping combined, which counts the difference of occurences between s and t
        mapping_combined = {}
        for i in mapping_t:
            if i in mapping_s:
                mapping_combined[i] = mapping_t[i] - mapping_s[i]
            else:
                mapping_combined[i] = mapping_t[i]
        # return the letter in mapping combined, in which the value is 1
        for i in mapping_combined:
            if mapping_combined[i] ==1:
                return i
                
                
opt = Solution()
print(opt.findTheDifference('abcd','abcde'))
