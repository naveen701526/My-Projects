class Solution:
    def findDisappearedNumbers(self, nums):
        ans = []
        for val in nums:
            temp = abs(val)
            if nums[temp - 1] > 0:
                nums[temp - 1] = -nums[temp - 1]
        for i, val in enumerate(nums):
            if val > 0:
                ans.append(i+1)
        return ans


obj = Solution()
print(obj.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
