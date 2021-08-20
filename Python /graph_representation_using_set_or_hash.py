# Python3 program to represent adjacency
# list using dictionary
class graph(object):

	def __init__(self, v):
		
		self.v = v
		self.graph = dict()

	# Adds an edge to undirected graph
	def addEdge(self, source, destination):
		
		# Add an edge from source to destination.
		# If source is not present in dict add source to dict
		if source not in self.graph:
			self.graph = {destination}
		else:
			self.graph.add(destination)

		# Add an dge from destination to source.
		# If destination is not present in dict add destination to dict
		if destination not in self.graph:
			self.graph[destination] = {source}
		else:
			self.graph[destination].add(source)

	# A utility function to print the adjacency
	# list representation of graph
	def print(self):
		
		for i, adjlist in sorted(self.graph.items()):
			print("Adjacency list of vertex ", i)
			for j in sorted(adjlist, reverse = True):
					print(j, end = " ")
						
			print('\n')
			
	# Search for a given edge in graph
	def searchEdge(self,source,destination):
		
		if source in self.graph:
			if destination in self.graph:
				if destination in self.graph:
					if source in self.graph[destination]:
						print("Edge from {0} to {1} found.\n".format(source, destination))
						return
					else:
						print("Edge from {0} to {1} not found.\n".format(source, destination))
						return
				else:
					print("Edge from {0} to {1} not found.\n".format(source, destination))
					return
			else:
				print("Destination vertex {} is not present in graph.\n".format(destination))
				return
		else:
			print("Source vertex {} is not present in graph.\n".format(source))
		
# Driver code
if __name__=="__main__":
	
	g = graph(5)
	
	g.addEdge(0, 1)
	g.addEdge(0, 4)
	g.addEdge(1, 2)
	g.addEdge(1, 3)
	g.addEdge(1, 4)
	g.addEdge(2, 3)
	g.addEdge(3, 4)

	# Print adjacenecy list
	# representation of graph
	g.print()

	# Search the given edge in a graph
	g.searchEdge(2, 1)
	g.searchEdge(0, 3)
