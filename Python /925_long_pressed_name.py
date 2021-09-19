class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        c, v = name[0], []
        if name[-1] != typed[-1]:
            return False
        for i in name[1:]:
            if i == c[0]:
                c += i
            else:
                v.append(c)
                c = i
        v.append(c)
        c, j = typed[0], 0
        for i in typed[1:]:
            if i == c[0]:
                c += i
            else:
                try:
                    if v[j] not in c:
                        return False
                    j += 1
                    c = i
                except:
                    return False
        if v[j] not in c:
            return False
        if j < len(v)-1:
            return False
        return True
        
        
opt = Solution()
print(opt.isLongPressedName('alex','aaleex'))
