# A Dynamic programming based Python3
# program to count derangements

def countDer(n):
	
	# Create an array to store
	# counts for subproblems
	der = [0 for i in range(n + 1)]
	
	# Base cases
	der[1] = 0
	der[2] = 1
	
	# Fill der[0..n] in bottom up manner
	# using above recursive formula
	for i in range(3, n + 1):
		der[i] = (i - 1) * (der[i - 1] +
							der[i - 2])
		
	# Return result for n
	return der[n]

# Driver Code
n = 4
print("Count of Derangements is ", countDer(n))
