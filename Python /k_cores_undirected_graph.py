# Python program to find K-Cores of a graph
from collections import defaultdict

# This class represents a undirected graph using adjacency
# list representation


class Graph:

	def __init__(self):

		# default dictionary to store graph
		self.graph = defaultdict(list)

	# function to add an edge to undirected graph
	def addEdge(self, u, v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	# A recursive function to call DFS starting from v.
	# It returns true if vDegree of v after processing is less
	# than k else false
	# It also updates vDegree of adjacent if vDegree of v
	# is less than k. And if vDegree of a processed adjacent
	# becomes less than k, then it reduces of vDegree of v also,
	def DFSUtil(self, v, visited, vDegree, k):

		# Mark the current node as visited
		visited.add(v)

		# Recur for all the vertices adjacent to this vertex
		for i in self.graph[v]:

			# vDegree of v is less than k, then vDegree of
			# adjacent must be reduced
			if vDegree[v] < k:
				vDegree[i] = vDegree[i] - 1

			# If adjacent is not processed, process it
			if i not in visited:

				# If vDegree of adjacent after processing becomes
				# less than k, then reduce vDegree of v also
				self.DFSUtil(i, visited, vDegree, k)

	def PrintKCores(self, k):

		visit = set()
		degree = defaultdict(lambda: 0)

		for i in list(self.graph):
			degree[i] = len(self.graph[i])

		for i in list(self.graph):

			if i not in visit:
				self.DFSUtil(i, visit, degree, k)

		# print(degree)
		# print(self.graph)

		for i in list(self.graph):

			if degree[i] >= k:
				print(str("\n [ ") + str(i) + str(" ]"), end=" ")

				for j in self.graph[i]:
					if degree[j] >= k:
						print("-> " + str(j), end=" ")

				print()


k = 3
g1 = Graph()
g1.addEdge(0, 1)
g1.addEdge(0, 2)
g1.addEdge(1, 2)
g1.addEdge(1, 5)
g1.addEdge(2, 3)
g1.addEdge(2, 4)
g1.addEdge(2, 5)
g1.addEdge(2, 6)
g1.addEdge(3, 4)
g1.addEdge(3, 6)
g1.addEdge(3, 7)
g1.addEdge(4, 6)
g1.addEdge(4, 7)
g1.addEdge(5, 6)
g1.addEdge(5, 8)
g1.addEdge(6, 7)
g1.addEdge(6, 8)
g1.PrintKCores(k)
