# Python3 program to connect n
# ropes with minimum cost
import heapq

def minCost(arr, n):
	
	# Create a priority queue out of the
	# given list
	heapq.heapify(arr)
	
	# Initializ result
	res = 0
	
	# While size of priority queue
	# is more than 1
	while(len(arr) > 1):
		
		# Extract shortest two ropes from arr
		first = heapq.heappop(arr)
		second = heapq.heappop(arr)
		
		#Connect the ropes: update result
		# and insert the new rope to arr
		res += first + second
		heapq.heappush(arr, first + second)
		
	return res

# Driver code
if __name__ == '__main__':
	
	lengths = [ 4, 3, 2, 6 ]
	size = len(lengths)
	
	print("Total cost for connecting ropes is " +
		str(minCost(lengths, size)))
