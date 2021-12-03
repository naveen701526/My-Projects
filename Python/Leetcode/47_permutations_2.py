class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return self.dfs(sorted(nums), [], [])

    def dfs(self, nums: List[int], path: List[int], res: List[List[int]]) -> List[List[int]]:
        if not nums: res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
        return res
