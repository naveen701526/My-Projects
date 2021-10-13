# Python3 Program to determine level
# of each node and print level
import queue

# function to determine level of
# each node starting from x using BFS
def printLevels(graph, V, x):
	
	# array to store level of each node
	level = [None] * V
	marked = [False] * V

	# create a queue
	que = queue.Queue()

	# enqueue element x
	que.put(x)

	# initialize level of source
	# node to 0
	level[x] = 0

	# marked it as visited
	marked[x] = True

	# do until queue is empty
	while (not que.empty()):

		# get the first element of queue
		x = que.get()

		# traverse neighbors of node x
		for i in range(len(graph[x])):
			
			# b is neighbor of node x
			b = graph[x][i]

			# if b is not marked already
			if (not marked[b]):

				# enqueue b in queue
				que.put(b)

				# level of b is level of x + 1
				level[b] = level[x] + 1

				# mark b
				marked[b] = True

	# display all nodes and their levels
	print("Nodes", " ", "Level")
	for i in range(V):
		print(" ",i, " --> ", level[i])

# Driver Code
if __name__ == '__main__':

	# adjacency graph for tree
	V = 8
	graph = [[] for i in range(V)]

	graph[0].append(1)
	graph[0].append(2)
	graph[1].append(3)
	graph[1].append(4)
	graph[1].append(5)
	graph[2].append(5)
	graph[2].append(6)
	graph[6].append(7)

	# call levels function with source as 0
	printLevels(graph, V, 0)

