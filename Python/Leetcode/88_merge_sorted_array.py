class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        while n > 0 and m > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n-=1
            last -= 1
            
        while n > 0:
            nums1[last] = nums2[n-1]
            n-=1
            last-=1
            
        return nums1
        
opt = Solution()
print(opt.merge([1,2,3,0,0,0], 3, [2,5,6],  3))
