# Python3 implementation to rearrange
# the array elements after modification

# function which pushes all zeros
# to end of an array.
def pushZerosToEnd(arr, n):

	# Count of non-zero elements
	count = 0

	# Traverse the array. If element
	# encountered is non-zero, then
	# replace the element at index
	# 'count' with this element
	for i in range(0, n):
		if arr[i] != 0:

			# here count is incremented
			arr[count] = arr[i]
			count+=1

	# Now all non-zero elements have been
	# shifted to front and 'count' is set
	# as index of first 0. Make all
	# elements 0 from count to end.
	while (count < n):
		arr[count] = 0
		count+=1


# function to rearrange the array
# elements after modification
def modifyAndRearrangeArr(ar, n):

	# if 'arr[]' contains a single
	# element only
	if n == 1:
		return

	# traverse the array
	for i in range(0, n - 1):

		# if true, perform the required modification
		if (arr[i] != 0) and (arr[i] == arr[i + 1]):

			# double current index value
			arr[i] = 2 * arr[i]

			# put 0 in the next index
			arr[i + 1] = 0

			# increment by 1 so as to move two
			# indexes ahead during loop iteration
			i+=1

	

	# push all the zeros at the end of 'arr[]'
	pushZerosToEnd(arr, n)


# function to print the array elements
def printArray(arr, n):

	for i in range(0, n):
		print(arr[i],end=" ")


# Driver program to test above
arr = [ 0, 2, 2, 2, 0, 6, 6, 0, 0, 8 ]
n = len(arr)

print("Original array:",end=" ")
printArray(arr, n)

modifyAndRearrangeArr(arr, n)

print("\nModified array:",end=" ")
printArray(arr, n)
