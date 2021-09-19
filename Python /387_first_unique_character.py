class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict={}
        for i in range(len(s)):
	        if s[i] not in dict:
		        dict[s[i]]=[]
		        dict[s[i]].append(s.count(s[i]))
		        dict[s[i]].append(i)
        for key,value in dict.items():
	        if value[0]==1:
		        return value[1]
        return -1
        
opt = Solution()
print(opt.firstUniqChar("leetcode"))
