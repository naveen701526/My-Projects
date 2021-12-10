class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        space = sorted(candidates)
        
        def dfs(space,track,remain):
            if remain == 0:
                res.append(track)
            for i in range(len(space)):
                if space[i] > remain:
                    break
                if i > 0 and space[i] == space[i-1]:
                    continue
                dfs(space[i+1:],track+[space[i]],remain-space[i])
        
        dfs(space,[],target)
        return res
