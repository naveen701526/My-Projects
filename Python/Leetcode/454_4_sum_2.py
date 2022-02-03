class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        lookup = {}
        
		# Finding the 2sum and adding in lookup.
        for i in nums1:
            for j in nums2:
                s = i+j
                if s not in lookup:
                    lookup[s] = 0
                lookup[s] += 1
        
        ans = 0
		# Find the 2sum and checking in lookup whether the negative is present or not.
        for i in nums3:
            for j in nums4:
                s = i + j
                if -s in lookup:
                    ans += lookup[-s]
        
        return ans
