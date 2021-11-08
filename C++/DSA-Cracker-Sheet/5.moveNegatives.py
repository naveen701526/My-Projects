def moveNegative(array):
    left = 0
    right = len(array)-1
    while left < right:
        if array[left] < 0 and array[right] > 0:
            left += 1
            right -= 1
        elif array[left] > 0 and array[right] > 0:
            right -= 1
        elif array[left] < 0 and array[right] < 0:
            left += 1
        elif array[left] > 0 and array[right] < 0:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1

    return array


array = [int(x) for x in input().split(', ')]

print(moveNegative(array))
