# Python program to multiply all values in the
# list using traversal

def multiplyList(myList):

    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result


# Driver code
list1 = [int(x) for x in input().split()]

print(multiplyList(list1))
