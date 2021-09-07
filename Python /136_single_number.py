class Solution:
    def singleNumber(self, nums: [int]) -> int:
        output = 0
        for num in nums:
            output ^= num
            
        return output
        
        
opt = Solution()
print(opt.singleNumber([1,2,3,3,2]))
