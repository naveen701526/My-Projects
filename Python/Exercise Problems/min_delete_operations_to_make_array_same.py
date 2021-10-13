# Python3 program to find minimum
# number of deletes required to
# make all elements same.

# Function to get minimum number
# of elements to be deleted from
# array to make array elements equal
def minDelete(arr, n):
	
	# Create an dictionary and store
	# frequencies of all array
	# elements in it using
	# element as key and
	# frequency as value
	freq = {}
	for i in range(n):
		if arr[i] in freq:
			freq[arr[i]] += 1
		else:
			freq[arr[i]] = 1
		

	# Find maximum frequency
	# among all frequencies.
	max_freq = 0;
	for i, j in freq.items():
		max_freq = max(max_freq, j)

	# To minimize delete operations,
	# we remove all elements but the
	# most frequent element.
	return n - max_freq;
	
# Driver code
arr = [ 4, 3, 4, 4, 2, 4 ]
n = len(arr)

print(minDelete(arr, n))
