class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        #p1,p2 are pointers pointing at right end of string num1,num2
        p1, p2 = len(num1)-1, len(num2)-1
        #ret is a list stores the result of addition of two strings num1,num2
        ret = []
        #carry is used to carry out the digit after addtion of two digits in a number
        carry = 0
        #loop to add two numbers using carry
        while p1 >= 0 or p2 >= 0 or carry:
            #convert character of each string into an integer digit
            d1 = int(num1[p1]) if p1 >= 0 else 0
            d2 = int(num2[p2]) if p2 >= 0 else 0
            #add two digits and carry of previous sum
            sum = d1+d2+carry
            #carry is found by removing last digit of sum
            #digit is result of sum's last digit
            carry, digit = sum//10, sum%10
            #store the digit in ret list. But the answer will be reversed(right to left)
            # so reverse it again to get correct answer
            ret.append(str(digit))
            p1 -= 1
            p2 -= 1
            
        #convert the list into string using join method
        return "".join(ret[::-1])
        
        
opt = Solution()
print(opt.addStrings('11','112'))
print(opt.addStrings('99', '1'))
