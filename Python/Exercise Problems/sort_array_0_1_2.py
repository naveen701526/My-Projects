# Python implementation of the approach

# Utility function to print contents of an array
def printArr(arr, n):
	for i in range(n):
		print(arr[i],end=" ")


# Function to sort the array of 0s, 1s and 2s
def sortArr(arr, n):
	cnt0 = 0
	cnt1 = 0
	cnt2 = 0
	
	# Count the number of 0s, 1s and 2s in the array
	for i in range(n):
		if arr[i] == 0:
			cnt0+=1
		
		elif arr[i] == 1:
			cnt1+=1
			
		elif arr[i] == 2:
			cnt2+=1
	
	# Update the array
	i = 0
	
	# Store all the 0s in the beginning
	while (cnt0 > 0):
		arr[i] = 0
		i+=1
		cnt0-=1
	
	# Then all the 1s
	while (cnt1 > 0):
		arr[i] = 1
		i+=1
		cnt1-=1
	
	# Finally all the 2s
	while (cnt2 > 0):
		arr[i] = 2
		i+=1
		cnt2-=1
	
	# Prthe sorted array
	printArr(arr, n)


# Driver code

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
n = len(arr)

sortArr(arr, n)

