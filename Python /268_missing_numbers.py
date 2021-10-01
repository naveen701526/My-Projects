class Solution:
    def missingNumber(self, nums: [int]) -> int:
        # color the nums O(n)   O(1)
        nums = [x+1 for x in nums]
        for i in nums:
            if 0 <= abs(i) < len(nums)+1:
                nums[abs(i)-1] *= -1
        for i in range(len(nums)):
            if nums[i] > 0:
                return i
        return len(nums)
        
        
opt = Solution()
print(opt.missingNumber(nums = [3,0,1]))
