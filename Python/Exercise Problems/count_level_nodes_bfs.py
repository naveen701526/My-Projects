# Python3 program to print
# count of nodes at given level.
from collections import deque

adj = [[] for i in range(1001)]

def addEdge(v, w):
	
	# Add w to v’s list.
	adj[v].append(w)

	# Add v to w's list.
	adj[w].append(v)

def BFS(s, l):
	
	V = 100
	
	# Mark all the vertices
	# as not visited
	visited = [False] * V
	level = [0] * V

	for i in range(V):
		visited[i] = False
		level[i] = 0

	# Create a queue for BFS
	queue = deque()

	# Mark the current node as
	# visited and enqueue it
	visited[s] = True
	queue.append(s)
	level[s] = 0

	while (len(queue) > 0):
		
		# Dequeue a vertex from
		# queue and prit
		s = queue.popleft()
		#queue.pop_front()

		# Get all adjacent vertices
		# of the dequeued vertex s.
		# If a adjacent has not been
		# visited, then mark it
		# visited and enqueue it
		for i in adj[s]:
			if (not visited[i]):

				# Setting the level
				# of each node with
				# an increment in the
				# level of parent node
				level[i] = level[s] + 1
				visited[i] = True
				queue.append(i)

	count = 0
	for i in range(V):
		if (level[i] == l):
			count += 1
			
	return count

# Driver code
if __name__ == '__main__':
	
	# Create a graph given
	# in the above diagram
	addEdge(0, 1)
	addEdge(0, 2)
	addEdge(1, 3)
	addEdge(2, 4)
	addEdge(2, 5)

	level = 2

	print(BFS(0, level))
