# Python3 code to demonstrate working of
# Remove Tuples of Length K
# Using list comprehension

# initializing list
test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]

# printing original list
print("The original list : " + str(test_list))

# initializing K
K = 1

# 1 liner to perform task
# filter just lengths other than K
# len() used to compute length
res = [ele for ele in test_list if len(ele) != K]

# printing result
print("Filtered list : " + str(res))
