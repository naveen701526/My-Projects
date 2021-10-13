def first_missing_number(nums):
    if len(nums) == 0:
        return 1

    nums.sort()
    smallest_int_num = 0

    for i in range(len(nums) - 1):

        if nums[i] <= 0 or nums[i] == nums[i + 1]:
            continue
        else:
            if nums[i + 1] - nums[i] != 1:
                smallest_int_num = nums[i] + 1
                return smallest_int_num
    if smallest_int_num == 0:
        smallest_int_num = nums[-1] + 1
    return smallest_int_num


print(first_missing_number([int(x) for x in input().split()]))
