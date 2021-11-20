class Solution:
    def singleNonDuplicate(self, nums) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left)//2
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]

            if (mid % 2 == 0 and nums[mid] == nums[mid+1]) or (mid % 2 == 1 and nums[mid] == nums[mid-1]):
                left = mid + 1
            else:
                right = mid - 1


obj = Solution()
print(obj.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]))
