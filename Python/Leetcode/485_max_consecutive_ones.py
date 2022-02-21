class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_so_far = 0
        current_max = 0
        for num in nums:
            if num:
                current_max+=1
            else:
                max_so_far = max(max_so_far, current_max)
                current_max = 0
        return max(current_max, max_so_far)
