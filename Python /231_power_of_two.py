class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1:
            return False
        return self.isPowerOfTwo(n/2)
        
        
opt = Solution()
print(opt.isPowerOfTwo(45))
print(opt.isPowerOfTwo(8))
