# Python3 program to implement recursive
# randomized algorithm.
# To generate random number
# between x and y ie.. [x, y]

import random
def getRandom(x,y):
	tmp=(x + random.randint(0,100000) % (y-x+1))
	return tmp
	
# A recursive randomized binary search function.
# It returns location of x in
# given array arr[l..r] is present, otherwise -1

def randomizedBinarySearch(arr,l,r,x) :
	if r>=l:
		
		# Here we have defined middle as
		# random index between l and r ie.. [l, r]
		mid=getRandom(l,r)
		
		# If the element is present at the
		# middle itself
		if arr[mid] == x:
			return mid
			
		# If element is smaller than mid, then
		# it can only be present in left subarray
		if arr[mid]>x:
			return randomizedBinarySearch(arr, l, mid-1, x)
			
		# Else the element can only be present
		# in right subarray
		return randomizedBinarySearch(arr, mid+1,r, x)
		
	# We reach here when element is not present
	# in array
	return -1
	
# Driver code
if __name__=='__main__':
	arr = [2, 3, 4, 10, 40]
	n=len(arr)
	x=10
	result = randomizedBinarySearch(arr, 0, n-1, x)
	if result==-1:
		print('Element is not present in array')
	else:
		print('Element is present at index ', result)
		
