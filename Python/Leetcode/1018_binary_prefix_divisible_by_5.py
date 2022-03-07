class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        if nums[0] == 0:
            res.append(True)
        else:
            res.append(False)
        current = nums[0]
        for i in range(1,len(nums)):
            current = 2*current + nums[i]
            if current%5==0:
                res.append(True)
            else:
                res.append(False)
        return res
