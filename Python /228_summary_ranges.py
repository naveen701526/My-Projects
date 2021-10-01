class Solution:
    def summaryRanges(self, nums: [int]) -> [str]:
        l, v, j = [], [], 0
        while j < len(nums):
            if v != []: 
                if nums[j] - 1 == v[-1]:
                    v += [nums[j]]
                    j += 1
                else:
                    l += [v]
                    v = []
            else:
                v += [nums[j]]
                j += 1
        if v != []:
            l += [v]
        v = []
        for i in l:
            if len(i) == 1:
                v.append(str(*(i)))
            else:
                v.append(str(i[0])+'->'+str(i[-1]))
        return(v)
        
        
opt = Solution()
print(opt.summaryRanges(nums = [0,1,2,4,5,7]))
