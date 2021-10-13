#Python3 program to count total number of
#special sequences of length n where
#Recursive function to find the number of
# special sequences
def getTotalNumberOfSequences(m,n):

	#A special sequence cannot exist if length
	#n is more than the maximum value m.
	if m<n:
		return 0

	#If n is 0, found an empty special sequence
	if n==0:
		return 1

	#There can be two possibilities : (1) Reduce
	#last element value (2) Consider last element
	#as m and reduce number of terms
	res=(getTotalNumberOfSequences(m-1,n)+
		getTotalNumberOfSequences(m//2,n-1))
	return res

#Driver Code
if __name__=='__main__':
	m=10
	n=4
	print('Total number of possible sequences:',getTotalNumberOfSequences(m,n))
