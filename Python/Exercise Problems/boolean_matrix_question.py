# Python3 Code For A Boolean Matrix Question
def modifyMatrix(mat) :
	
	# variables to check if there are any 1
	# in first row and column
	row_flag = False
	col_flag = False
			
	# updating the first row and col
	# if 1 is encountered
	for i in range(0, len(mat)) :
		
		for j in range(0, len(mat)) :
			if (i == 0 and mat[i][j] == 1) :
				row_flag = True
					
			if (j == 0 and mat[i][j] == 1) :
				col_flag = True
			
			if (mat[i][j] == 1) :
				mat[0][j] = 1
				mat[i][0] = 1
				
	# Modify the input matrix mat[] using the
	# first row and first column of Matrix mat
	for i in range(1, len(mat)) :
		
		for j in range(1, len(mat) + 1) :
			if (mat[0][j] == 1 or mat[i][0] == 1) :
				mat[i][j] = 1
				
	# modify first row if there was any 1
	if (row_flag == True) :
		for i in range(0, len(mat)) :
			mat[0][i] = 1
			
	# modify first col if there was any 1
	if (col_flag == True) :
		for i in range(0, len(mat)) :
			mat[i][0] = 1
			
# A utility function to print a 2D matrix
def printMatrix(mat) :
	
	for i in range(0, len(mat)) :
		for j in range(0, len(mat) + 1) :
			print( mat[i][j], end = "" )
		
		print()
		
# Driver Code
mat = [ [1, 0, 0, 1],
		[0, 0, 1, 0],
		[0, 0, 0, 0] ]
		
print("Input Matrix :")
printMatrix(mat)
	
modifyMatrix(mat)
	
print("Matrix After Modification :")
printMatrix(mat)
