class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        j = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i+1]:
                nums[j] = nums[i+1]
                j+=1
        
        return j
            
opt = Solution()
print(opt.removeDuplicates([1,1,2]))
print(opt.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
