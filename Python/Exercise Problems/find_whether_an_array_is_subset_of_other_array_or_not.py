# Python 3 program to find whether an array
# is subset of another array

# Return 1 if arr2[] is a subset of
# arr1[]
def isSubset(arr1, arr2, m, n):
	i = 0
	j = 0
	for i in range(n):
		for j in range(m):
			if(arr2[i] == arr1[j]):
				break
		
		# If the above inner loop was
		# not broken at all then arr2[i]
		# is not present in arr1[]
		if (j == m):
			return 0
	
	# If we reach here then all
	# elements of arr2[] are present
	# in arr1[]
	return 1

# Driver code
if __name__ == "__main__":
	
	arr1 = [11, 1, 13, 21, 3, 7]
	arr2 = [11, 3, 7, 1]

	m = len(arr1)
	n = len(arr2)

	if(isSubset(arr1, arr2, m, n)):
		print("arr2[] is subset of arr1[] ")
	else:
		print("arr2[] is not a subset of arr1[]")
