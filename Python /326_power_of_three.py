# https://leetcode.com/problems/power-of-three/
class Solution:
    def isPowerOfThree(self, n: int,) -> bool:
        if n == 1:
            return True
        if n < 1:
            return False
        return self.isPowerOfThree(n/3)
            
opt = Solution()
print(opt.isPowerOfThree(45))
print(opt.isPowerOfThree(1))
print(opt.isPowerOfThree(3))
print(opt.isPowerOfThree(0))
print(opt.isPowerOfThree(81))
