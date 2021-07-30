# Python3 code to demonstrate working of
# Convert Nested Tuple to Custom Key Dictionary
# Using list comprehension + dictionary comprehension

# initializing tuple
test_tuple = ((4, 'Gfg', 10), (3, 'is', 8), (6, 'Best', 10))

# printing original tuple
print("The original tuple : " + str(test_tuple))

# Convert Nested Tuple to Custom Key Dictionary
# Using list comprehension + dictionary comprehension
res = [{'key': sub[0], 'value': sub[1], 'id': sub[2]}
							for sub in test_tuple]

# printing result
print("The converted dictionary : " + str(res))
