class Solution:
    def moveZeroes(self, nums: [int]) -> None:
        for y in nums:
            if y == 0:
                nums.append(0)
                nums.remove(0)
        print(nums)
                
opt = Solution()
opt.moveZeroes(nums = [0,1,0,3,12])
