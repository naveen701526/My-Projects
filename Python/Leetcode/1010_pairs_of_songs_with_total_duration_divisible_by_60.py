class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hashmap = defaultdict(int)
        for t in time:
            hashmap[t%60] += 1
        
        res = 0
        for t in time:
            reminder = t%60
            hashmap[reminder] -= 1
                
            res += hashmap[0 if reminder == 0 else 60 - reminder]
                
        return res
