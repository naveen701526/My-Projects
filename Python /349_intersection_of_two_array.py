class Solution:
    def intersection(self, nums1: [int], nums2: [int]) -> [int]:
        return list(set(nums1).intersection(set(nums2)))
        
        
        
opt = Solution()
print(opt.intersection([1,2,2,1],[2,2]))
print(opt.intersection([4,9,5],[9,4,9,8,4]))
