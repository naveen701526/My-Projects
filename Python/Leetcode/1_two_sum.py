class Solution:
    def twoSum(self, nums: [int], target: int) -> [int]:
        map = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in map: return [map[val], i]
            else: map[nums[i]] = i
        return []
        
opt = Solution()
print(opt.twoSum(nums = [2,7,11,15], target = 9))
