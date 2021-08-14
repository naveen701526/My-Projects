# Python3 program to construct an n x n
# matrix such that every row and every
# column has distinct values.

MAX = 100;
mat = [[0 for x in range(MAX)] for y in range(MAX)];

# Fills non-one entries in column j
# Given that there is a "1" at
# position mat[i][j], this function
# fills other entries of column j.
def fillRemaining(i, j, n):

	# Initialize value to be filled
	x = 2;

	# Fill all values below i as 2, 3, ...p
	for k in range(i + 1,n):
		mat[k][j] = x;
		x+=1;

	# Fill all values above i
	# as p + 1, p + 2, .. n
	for k in range(i):
		mat[k][j] = x;
		x+=1;

# Fills entries in mat[][]
# with the given set of rules
def constructMatrix(n):

	# Alternatively fill 1s starting from
	# rightmost and leftmost columns. For
	# example for n = 3, we get { {_ _ 1},
	# {1 _ _} {_ 1 _}}
	right = n - 1;
	left = 0;
	for i in range(n):
		# If i is even, then fill
		# next column from right
		if (i % 2 == 0):
			mat[i][right] = 1;

			# After filling 1, fill remaining
			# entries of column "right"
			fillRemaining(i, right, n);

			# Move right one column back
			right-=1;
		
		# Fill next column from left
		else:
			mat[i][left] = 1;

			# After filling 1, fill remaining
			# entries of column "left"
			fillRemaining(i, left, n);

			# Move left one column forward
			left+=1;

# Driver code
n = 5;

# Passing n to constructMatrix function
constructMatrix(n);

# Printing the desired unique matrix
for i in range(n):
	for j in range(n):
		print(mat[i][j],end=" ");
	print("");
	
