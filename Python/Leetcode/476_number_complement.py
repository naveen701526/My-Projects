class Solution:
    def findComplement(self, num: int) -> int:
        bi = bin(num).lstrip('0').lstrip('b')
        s=''
        for i in bi:
            if i=='1':
                s=s+'0'
            else:
                s=s+'1'
            
        return int(s,2)
