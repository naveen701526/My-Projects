class Solution:
    def countBits(self, n: int) -> [int]:
        ans = [0] * (n + 1) #memory to store result previous values
        offset = 1 #power of two initially 2^0
        for i in range(1,n+1):
            if offset * 2 == i: #i is power of 2 checking
                offset = i  #increment offset to i
            ans[i] = 1 + ans[i - offset]
            
        return ans
        
        
opt = Solution()
print(opt.countBits(n = 2))
print(opt.countBits(n = 5))
