def findSplitIndex(array, length):
    summation = 0
    for index in range(length):
        summation += array[index]
        
    leftSum = summation
    rightSum = 0
    
    for index in range(length-1, -1, -1):
        rightSum += array[index]
        leftSum -= array[index]
        
        if leftSum == rightSum:
            return index
            
    return -1
    
# Example to check whether the function works or not
print(findSplitIndex([1,2,3,4,5,5], 6))
print(findSplitIndex([4,1,2,3], 4))
print(findSplitIndex([4,3,2,1], 4))


# time complexity: O(n)
# space complexity: O(1)
