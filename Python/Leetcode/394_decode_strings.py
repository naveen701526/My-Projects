class Solution:
    def decodeString(self, s: str) -> str:
        i=0
        res=""
        multiplier=1
        # print(s)
        while i<len(s):
            # print(s[i])
            if s[i]>="a" and s[i]<="z":
                res+=s[i]
                i+=1
            elif s[i]=="[":
                innerString=""
                i+=1
                brackets=0
                while s[i]!="]" or brackets!=0:
                    innerString+=s[i]
                    if s[i]=="[":
                        brackets+=1
                    elif s[i]=="]":
                        brackets-=1
                    i+=1
                i+=1
                res+=multiplier*self.decodeString(innerString)
            else:
                multiplier=int(s[i])
                i+=1
                while s[i]!="[":
                    multiplier=multiplier*10+int(s[i])
                    i+=1
        return res
