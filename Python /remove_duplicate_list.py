# Using set()
list_1 = [1, 2, 1, 4, 6]

print(list(set(list_1)))


# Remove the items that are duplicated


list_2 = [7, 8, 2, 1]

print(list(set(list_1) ^ set(list_2) ))
