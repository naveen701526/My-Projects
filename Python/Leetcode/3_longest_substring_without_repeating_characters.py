class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #find the last index in our hashMap
        hashMap = {}
        i, j,n=0,0,len(s)
        mx_len = 0
        while j < n:
            while j<n:
                if (s[j] in hashMap and hashMap[s[j]] < i) or s[j] not in hashMap:
                    hashMap[s[j]] = j
                    j+=1
                else:
                    break
            mx_len = max(mx_len, j-i)
            i = hashMap[s[j]]+1 if j<n else None
        return mx_len
        
opt = Solution()
print(opt.lengthOfLongestSubstring(s = "abcabcbb"))
print(opt.lengthOfLongestSubstring(s = "bbbbb"))
print(opt.lengthOfLongestSubstring(s = "pwwkew"))
print(opt.lengthOfLongestSubstring(s = ""))
