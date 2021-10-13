# Python3 program to merge two Max heaps.

# Standard heapify function to heapify a
# subtree rooted under idx. It assumes that
# subtrees of node are already heapified.
def MaxHeapify(arr, n, idx):
	
	# Find largest of node and
	# its children
	if idx >= n:
		return
	l = 2 * idx + 1
	r = 2 * idx + 2
	Max = 0
	if l < n and arr[l] > arr[idx]:
		Max = l
	else:
		Max = idx
	if r < n and arr[r] > arr[Max]:
		Max = r

	# Put Maximum value at root and
	# recur for the child with the
	# Maximum value
	if Max != idx:
		arr[Max], arr[idx] = arr[idx], arr[Max]
		MaxHeapify(arr, n, Max)

# Builds a Max heap of given arr[0..n-1]
def buildMaxHeap(arr, n):
	
	# building the heap from first non-leaf
	# node by calling Max heapify function
	for i in range(int(n / 2) - 1, -1, -1):
		MaxHeapify(arr, n, i)

# Merges Max heaps a[] and b[] into merged[]
def mergeHeaps(merged, a, b, n, m):
	
	# Copy elements of a[] and b[] one
	# by one to merged[]
	for i in range(n):
		merged[i] = a[i]
	for i in range(m):
		merged[n + i] = b[i]

	# build heap for the modified
	# array of size n+m
	buildMaxHeap(merged, n + m)

# Driver code
if __name__ == '__main__':
	a = [10, 5, 6, 2]
	b = [12, 7, 9]

	n = len(a)
	m = len(b)

	merged = [0] * (m + n)
	mergeHeaps(merged, a, b, n, m)

	for i in range(n + m):
		print(merged[i], end = " ")
