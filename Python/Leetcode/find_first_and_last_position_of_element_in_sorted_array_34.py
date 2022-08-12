class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List
        :type target: List
        :rtype List:
        """
        l = len(nums)
        lo, hi = 0, l-1
        res = [-1, -1]
        while lo <= hi:
            mid = (lo+hi)//2
            m = nums[mid]
            if m < target:
                lo = mid+1
            elif m > target:
                hi = mid-1
            else:
                res = [mid,mid]
                break
        while nums and res[1] < l-1 and nums[res[1]+1] == target:
            res[1] += 1
        while res[0] > 0 and nums and nums[res[0]-1] == target:
            res[0] -= 1
        return res
