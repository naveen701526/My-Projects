# Problem Statment ---> https://leetcode.com/problems/perfect-number/
import math
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<=1:
            return False
        answer = 1
        for i in range(2,int(math.sqrt(num))+1):
            if num%i==0:
                answer+=i+num//i
        return answer == num
        
obj = Solution()
print(obj.checkPerfectNumber(28))