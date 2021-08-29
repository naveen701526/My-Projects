#https://leetcode.com/problems/subarray-sum-equals-k/
def subarraySum(nums: [int], k: int) -> int:
    sumdict = {0:1}
        
    count = 0
    s = 0
    for num in nums:
        s += num
        if s - k in sumdict:
            count += sumdict[s-k]
        sumdict[s] = sumdict.get(s,0) + 1
    return count
            
            
print(subarraySum([1,2,3],3))        
