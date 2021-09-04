# Simple Python program
# to print squares
# of diagonal elements.

# function of diagonal square
def diagonalsquare(mat, row, column) :

	# This loop is for finding square
	# of first diagonal elements
	print ("Diagonal one : ", end = "")
	for i in range(0, row) :
		for j in range(0, column) :

			# if this condition will
			# become true then we will
			# get diagonal element
			if (i == j) :
				# printing square of
				# diagonal element
				print ("{} ".format(mat[i][j] *
									mat[i][j]), end = "")

	# This loop is for finding
	# square of second side
	# of diagonal elements
	print (" \n\nDiagonal two : ", end = "")
	for i in range(0, row) :
		for j in range(0, column) :

			# if this condition will become
			# true then we will get second
			# side diagonal element
			if (i + j == column - 1) :

				# printing square of diagonal
				# element
				print ("{} ".format(mat[i][j] *
									mat[i][j]), end = "")


# Driver code
mat = [[ 2, 5, 7 ],
		[ 3, 7, 2 ],
		[ 5, 6, 9 ]]
diagonalsquare(mat, 3, 3)
