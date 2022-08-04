# DFS (Depth First Search)
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def showEdge(self):
        print(self.graph)

    def DFS_helper(self, v, visited):
        visited[v] = True
        print(v)

        for i in self.graph[v]:
            if visited[i] == False:
                self.DFS_helper(i, visited)

    def DFS(self, v):
        visited = [False] * len(self.graph)
        self.DFS_helper(v, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 0)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 1)
g.addEdge(2, 3)
g.addEdge(3, 2)
g.showEdge()
g.DFS(2)
