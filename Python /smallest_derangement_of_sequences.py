# Efficient Python3 program to find
# smallest derangement.

def generate_derangement(N):
	
	# Generate Sequence S
	S = [0] * (N + 1)
	for i in range(1, N + 1):
		S[i] = i

	# Generate Derangement
	D = [0] * (N + 1)
	for i in range(1, N + 1, 2):
		if i == N:

			# Only if i is odd
			# Swap S[N-1] and S[N]
			D[N] = S[N - 1]
			D[N - 1] = S[N]
		else:
			D[i] = i + 1
			D[i + 1] = i

	# Print Derangement
	for i in range(1, N + 1):
		print(D[i], end = " ")
	print()

# Driver Code
if __name__ == '__main__':
	generate_derangement(10)
	
