class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []
        target = len(graph) - 1
        stack = [([0], graph[0])]

        while stack:
            for _ in range(len(stack)):
                path, nodes = stack.pop()
                if path and path[-1] == target:
                    result.append(path)
                for neighbor in nodes:
                    stack.append((path + [neighbor], graph[neighbor]))
        return result
