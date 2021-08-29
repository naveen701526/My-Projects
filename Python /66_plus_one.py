# https://leetcode.com/problems/plus-one/
def plusOne(digits):
    digits = [str(i) for i in digits]
    number = int(''.join(digits))
    number += 1
    number = str(number)
    digits = [int(i) for i in number]
    return digits
    
print(plusOne([9,9]))
print(plusOne([1,2,3]))
