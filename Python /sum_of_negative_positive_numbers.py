def count_sum(nums):
    if not nums:
        return []
    return [len([n for n in nums if n < 0]), sum(n for n in nums if n > 0)]


print(count_sum([int(x) for x in input().split()]))
