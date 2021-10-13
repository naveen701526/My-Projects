# Python program to find sum of
# middle row and column in matrix


def middlesum(mat,n):

	row_sum = 0
	col_sum = 0
	
	# loop for sum of row
	for i in range(n):
		row_sum += mat[n // 2][i]
	
	print("Sum of middle row = ",
					row_sum)
	
	# loop for sum of column
	for i in range(n):
		col_sum += mat[i][n // 2]
	
	print("Sum of middle column = ",
							col_sum)

# Driver code
mat= [[2, 5, 7],
	[3, 7, 2],
	[5, 6, 9]]
	
middlesum(mat, 3)
