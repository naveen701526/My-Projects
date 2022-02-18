class Solution:
    def isHappy(self, n: int) -> bool:
        b=[]
        for i in range(7):
            if n==1:
                return True
            a=list(str(n))
            n=sum(pow(int(i),2) for i in a)
            b.append(n)
        if len(set(b))!=len(b):
            return False
