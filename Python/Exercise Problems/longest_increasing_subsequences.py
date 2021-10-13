# Dyanmic Programming python3
# implementation of LIS problem

# lis() returns the length of the
# longest increasing subsequence
# in arr[] of size n
def lis(arr, n):
	i, j, maxm = 0, 0, 0
	
	# initialize LIS values for all indexes
	lst = [1 for s in range(n)]
	
	for i in range(1, n):
		for j in range(0, i):
			if (arr[i] > arr[j] and
				lst[i] < lst[j] + 1):
				lst[i] = lst[j] + 1
	
	# Pick maximum of all LIS values
	for i in range(0, n):
		if maxm < lst[i]:
			maxm = lst[i]
	
	return maxm

# Driver Code
arr = [10, 22, 9, 33, 21, 50, 41, 60]
n = len(arr)
print("Length of lst is", lis(arr, n))
