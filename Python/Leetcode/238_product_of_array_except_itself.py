class Solution:
    def productExceptSelf(self, nums):
        res = []
        
        acc = 1
        for n in nums:
            res.append(acc)
            acc *= n

        acc = 1
        for i in reversed(range(len(nums))):
            res[i] *= acc
            acc *= nums[i]
            
        return res


obj = Solution()
print(obj.productExceptSelf(nums = [1,2,3,4]))
