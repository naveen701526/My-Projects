class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hmap={}
        l=set()
        for i in range(len(s)):
            if s[i] not in hmap :
                if t[i]  in l:
                    return False
                else:
                    hmap[s[i]]=t[i]
                    l.add(t[i])
            else:
                if hmap[s[i]]!=t[i]:
                    return False
        return True
        
opt = Solution()
print(opt.isIsomorphic(s = "egg", t = "add"))
