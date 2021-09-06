
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        else:
            if n > 0:
                if n % 2 == 0:
                    temp = self.myPow(x,n/2)
                    return temp * temp
                else:
                    return x * self.myPow(x,n-1)
            if n < 0:
                n = abs(n)
                x = 1/x
                return x * self.myPow(x, n - 1)
                

opt = Solution()
print(opt.myPow(2,10))
