class Solution:
    
    def jump(self, nums: [int]) -> int:
        left = right = 0
        jumps = 0
        while right < len(nums) - 1:
            farthest = 0
            for i in range(left, right + 1):
                farthest = max(farthest, i + nums[i])
            left = right + 1
            right = farthest
            jumps += 1
        return jumps
            
obj = Solution()
print(obj.jump([2,3,1,1,4]))
        
