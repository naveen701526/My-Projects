class Solution:
    def findErrorNums(self, nums):
        res = 0
        for i in range(1, len(nums)+1):
            res ^= (i ^ nums[i-1])
        # Will give you the position of the rightmost set bit
        res = (res & -res)
        res1 = 0
        res2 = 0
        for i in range(len(nums)):
            if nums[i] & res > 0:
                res1 ^= nums[i]
            else:
                res2 ^= nums[i]
        for i in range(1, len(nums)+1):
            if i & res > 0:
                res1 ^= i
            else:
                res2 ^= i
        for i in range(len(nums)):
            if nums[i] == res1:
                return [res1, res2]
        return [res2, res1]


obj = Solution()
print(obj.findErrorNums(nums=[1, 2, 2, 4]))
