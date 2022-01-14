class Solution:
    def myAtoi(self, s: str) -> int:
        neg=1
        c=""
        flag=0
        for i in s:
            if i==' ':
                if flag>0:
                    break
                continue
            elif i.isalpha():
                flag+=1
                break
            elif i=='+':
                flag+=1
                if flag>=2:
                    break
            elif i=='-':
                flag+=1
                if flag>=2:
                    break
                neg=-1
            else:
                flag+=1
                c+=i
        if c=="":
            return 0
        res=int(float(c))
        if -2**(31)>res*neg:
            return -2**(31)
        if 2**(31)-1<res*neg:
            return 2**(31)-1
        return res*neg
