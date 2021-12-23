class Solution:
    """
    Kahn's algorithm
    """
    def findOrder(self, N: int, P: List[List[int]]) -> List[int]:
        
        # build graph
        graph = collections.defaultdict(set)
        in_degree = [0] * N
        for cos, pre in P:
            graph[pre].add(cos)
            in_degree[cos] += 1
            
        # initiate the container
        q = collections.deque()
        for cos, deg in enumerate(in_degree):
            if deg == 0:
                q.append(cos)
        print(q)       
        topo_ordering = []
        finished = 0
        while q:
            u = q.popleft()
            topo_ordering.append(u)
            finished += 1
            for v in graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
        print(topo_ordering)
        return topo_ordering if finished == N else []
