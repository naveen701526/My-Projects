class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums = collections.Counter(nums)
        
        res = 0
        for num in nums:
            
            if nums[num + 1]:
                res = max(res, nums[num] + nums[num + 1])   
                
        return res
