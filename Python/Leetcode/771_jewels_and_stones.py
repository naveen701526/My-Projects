class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        dict = {}
        
        for ele in jewels:
            if ele not in dict.keys():
                dict[ele] = 0
        
        for ele in stones:
            if ele in dict.keys():
                dict[ele] += 1
        
        count = 0
        for ele in dict.keys():
            count += dict[ele]
    
        return count
        
        
opt = Solution()
print(opt.numJewelsInStones(jewels = "aA", stones = "aAAbbbb"))
