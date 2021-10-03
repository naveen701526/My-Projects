import itertools
class Solution:
    def canJump(self, nums):
        t = list(itertools.accumulate([i + num for i, num in enumerate(nums)], max))
        return all(i != t[i] for i in range(len(t) - 1))
        
opt = Solution()
print(opt.canJump(nums = [2,3,1,1,4]))
print(opt.canJump(nums = [3,2,1,0,4]))

