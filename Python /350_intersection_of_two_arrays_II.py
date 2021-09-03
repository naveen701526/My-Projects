class Solution:
    def intersect(self, nums1: [int], nums2: [int]) -> [int]:
        
        output = []
        num1_occurence = {}
        num2_occurence = {}
        for num1 in nums1:
            num1_occurence[num1] = num1_occurence.get(num1, 0) + 1
        for num2 in nums2:
            num2_occurence[num2] = num2_occurence.get(num2, 0) + 1
        for num_occ in num1_occurence:
            if num2_occurence.get(num_occ, None):
                if num2_occurence[num_occ] == num1_occurence[num_occ]:
                    for i in range(num2_occurence[num_occ]):
                        output.append(num_occ)
                else:
                    val = min(num2_occurence[num_occ], num1_occurence[num_occ])
                    for i in range(val):
                        output.append(num_occ)
        return output
        
        
opt = Solution()
print(opt.intersect([2,1],[1,2]))
