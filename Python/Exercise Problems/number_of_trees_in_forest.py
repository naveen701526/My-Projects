# Python3 program to count number
# of trees in a forest.

# A utility function to add an
# edge in an undirected graph.
def addEdge(adj, u, v):
	adj[u].append(v)
	adj[v].append(u)

# A utility function to do DFS of graph
# recursively from a given vertex u.
def DFSUtil(u, adj, visited):
	visited[u] = True
	for i in range(len(adj[u])):
		if (visited[adj[u][i]] == False):
			DFSUtil(adj[u][i], adj, visited)

# Returns count of tree is the
# forest given as adjacency list.
def countTrees(adj, V):
	visited = [False] * V
	res = 0
	for u in range(V):
		if (visited[u] == False):
			DFSUtil(u, adj, visited)
			res += 1
	return res

# Driver code
if __name__ == '__main__':

	V = 5
	adj = [[] for i in range(V)]
	addEdge(adj, 0, 1)
	addEdge(adj, 0, 2)
	addEdge(adj, 3, 4)
	print(countTrees(adj, V))

