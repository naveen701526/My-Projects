# Python3 program to swap elements
# at given positions

# Swap function
def swapPositions(list, pos1, pos2):

    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


# Driver function
List = [int(x) for x in input().split()]
pos1, pos2 = input().split()

print(swapPositions(List, int(pos1)-1, int(pos2)-1))
