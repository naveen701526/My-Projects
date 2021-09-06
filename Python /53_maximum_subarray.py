class Solution:
    def maxSubArray(self, nums: [int]) -> int:
        maxsum = nums[0]
        maxyet = nums[0]
        for i in range(1,len(nums)):
            maxsum = max(maxsum + nums[i], nums[i])
            if maxsum > maxyet:
                maxyet = maxsum
        return maxyet
        
        
opt = Solution()
print(opt.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
