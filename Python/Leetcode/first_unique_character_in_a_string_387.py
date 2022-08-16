class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        
        
        for i in range(len(s)):
            if s[i] in dic:
                dic[s[i]]+=1
            else:
                dic[s[i]]=1
                
                
        for i in s:
            if dic[i]==1:
                return s.index(i)
            
        return -1    
