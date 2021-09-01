class Solution:
    def removeElement(self, nums, val):
        j =0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        print(nums)
        return j
        
        
opt = Solution()
print(opt.removeElement([3,2,2,3],3))
