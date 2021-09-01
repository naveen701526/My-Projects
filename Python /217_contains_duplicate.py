class Solution:
    def containsDuplicate(self, nums: [int]) -> bool:
        num_occurence = {}
        for num in nums:
            num_occurence[num] = num_occurence.get(num, 0) + 1
        for occurence in num_occurence:
            if num_occurence[occurence] >= 2:
                return True
        return False
        
opt = Solution()
print(opt.containsDuplicate([1,2,3,1]))
print(opt.containsDuplicate([1,2,3,4]))
