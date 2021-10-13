# Python code to demonstrate
# checking of element existence
# using loops and in

# Initializing list
test_list = [ 1, 6, 3, 5, 3, 4 ]

print("Checking if 4 exists in list ( using loop ) : ")

# Checking if 4 exists in list
# using loop
for i in test_list:
	if(i == 4) :
		print ("Element Exists")

print("Checking if 4 exists in list ( using in ) : ")

# Checking if 4 exists in list
# using in
if (4 in test_list):
	print ("Element Exists")
