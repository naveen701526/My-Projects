class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1, p2 = len(num1)-1, len(num2)-1
        ret = []
        carry = 0
        while p1 >= 0 or p2 >= 0 or carry:
            d1 = int(num1[p1]) if p1 >= 0 else 0
            d2 = int(num2[p2]) if p2 >= 0 else 0
            sum = d1+d2+carry
            carry, digit = sum//10, sum%10
            ret.append(str(digit))
            p1 -= 1
            p2 -= 1
            
        return "".join(ret[::-1])
        
        
opt = Solution()
print(opt.addStrings('11','112'))
print(opt.addStrings('99', '1'))
