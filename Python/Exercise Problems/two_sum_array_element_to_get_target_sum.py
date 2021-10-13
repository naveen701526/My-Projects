# Code in Python3 to tell if there
# exists a pair in array whose
# sum results in x.

# Function to print pairs
def printPairs(a, n, x):
	
	rem = []
	
	for i in range(x):

		# Initializing the rem
		# values with 0's.
		rem.append(0)

	for i in range(n):
		if (a[i] < x):

			# Perform the remainder operation
			# only if the element is x, as
			# numbers greater than x can't
			# be used to get a sum x.Updating
			# the count of remainders.
			rem[a[i] % x] += 1

	# Traversing the remainder list from
	# start to middle to find pairs
	for i in range(1, x // 2):
		if (rem[i] > 0 and rem[x - i] > 0):

			# The elements with remainders
			# i and x-i will result to a
			# sum of x. Once we get two
			# elements which add up to x,
			# we print x and break.
			print("Yes")
			break

	# Once we reach middle of
	# remainder array, we have to
	# do operations based on x.
	if (i >= x // 2):
		if (x % 2 == 0):
			if (rem[x // 2] > 1):

				# If x is even and we have more
				# than 1 elements with remainder
				# x/2, then we will have two
				# distinct elements which add up
				# to x. if we dont have than 1
				# element, print "No".
				print("Yes")
			else:
				print("No")
		else:

			# When x is odd we continue
			# the same process which we
			# did in previous loop.
			if (rem[x // 2] > 0 and
				rem[x - x // 2] > 0):
				print("Yes")
			else:
				print("No")

# Driver Code
A = [ 1, 4, 45, 6, 10, 8 ]
n = 16
arr_size = len(A)

# Function calling
printPairs(A, arr_size, n)
