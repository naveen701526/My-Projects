class Solution:
    def search(self, nums, target):
        start = len(nums)
        for i in range(len(nums)):
            if i < len(nums)-1 and nums[i] > nums[i+1]:
                start = i
                break
        if target < nums[0]:
            for i in nums[start:]:
                if target == i:
                    return True
            return False
        for i in nums[0:start+1]:
            if target == i:
                return True
        return False
