def remove_duplicates(nums):
    for i in range(len(nums)-1, 0, -1):
        if nums[i] == nums[i-1]:
            del nums[i-1]
    return len(nums)


print(remove_duplicates([int(x) for x in input().split()]))
