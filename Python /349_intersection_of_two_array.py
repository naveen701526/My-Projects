# class Solution:
#     def intersection(self, list1: [int], list2: [int]) -> [int]:
#         output = []
#         list1.sort()
#         list2.sort()
#         list1_pointer = 0
#         list2_pointer = 0
#         while list1_pointer<len(list1) and list2_pointer<len(list2):
#             if list1[list1_pointer] == list2[list2_pointer]:
#                 if len(output) == 0 or output[-1] != list1[list1_pointer]:
#                     output.append(list1[list1_pointer])
#                 list1_pointer+=1
#                 list2_pointer+=1
#             elif list1[list1_pointer] < list2[list2_pointer]:
#                 list1_pointer+=1
#             else:
#                 list2_pointer+=1
#         return output
# Approach - I
        


# Approach - II
class Solution:
    def intersection(self, nums1: [int], nums2: [int]) -> [int]:
        return list(set(nums1).intersection(set(nums2)))
        
        
        
opt = Solution()
print(opt.intersection([1,2,2,1],[2,2]))
print(opt.intersection([4,9,5],[9,4,9,8,4]))
