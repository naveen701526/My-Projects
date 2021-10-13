class Solution:
    def containsNearbyDuplicate(self, nums: [int], k: int) -> bool:
        
        dic = {}
        l = []
        
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i
            else:
                l.append(i - dic[nums[i]])
                dic[nums[i]] = i
        
        if not l:
            return False
        
        for num in l :
            if num <= k:
                return True
        
        return False
        
    
opt = Solution()
print(opt.containsNearbyDuplicate( nums = [1,2,3,1], k = 3))
