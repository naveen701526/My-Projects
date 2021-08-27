#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        sorted_nums = sorted(nums)
        smaller_element_counts = {}
        for index in range(len(sorted_nums)):
            smaller_element_counts[sorted_nums[index]] = smaller_element_counts.get(sorted_nums[index], index)
            
        new_nums = []
        for num in nums:
            new_nums.append(smaller_element_counts[num])
        return new_nums
        
        
output = Solution()

print(output.smallerNumbersThanCurrent([8,1,2,2,3]))
