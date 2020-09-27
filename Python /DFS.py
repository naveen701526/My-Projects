class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))

    def dfs(self, array):
        array.append(self.name)
        for child in self.children:
            child.dfs(array)
        return array


obj = Node('a')

for i in ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']:
    obj.add_child(i)
array = []
print(obj.dfs(array))
