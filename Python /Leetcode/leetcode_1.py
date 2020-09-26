def two_sum(nums, target):
    nums2 = []
    nums2 += nums
    nums.sort()

    nums1 = []
    r = len(nums) - 1
    l = 0
    while l < r:
        a = nums[l]
        b = nums[r]
        sum1 = a+b
        if sum1 == target:

            nums1.append(nums2.index(a))

            nums1.append(nums2.index(b))
            if nums1[0] == nums1[1]:
                nums1[1] = nums2.index(b, l+1, len(nums))
                return nums1
            else:
                return nums1
        elif sum1 < target:
            l += 1
        else:
            r -= 1


nums = [int(x) for x in input().split()]
target = int(input())
print(two_sum(nums, target))
