# BFS (Breadth First Search)
from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def showEdge(self):
        print(self.graph)

    def BFS(self, s):
        visited = [False] * (len(self.graph) + 1)
        nodes = []
        nodes.append(s)
        visited[s] = True

        while nodes:
            s = nodes.pop(0)
            print(s)
            for i in self.graph[s]:
                if not visited[i]:
                    nodes.append(i)
                    visited[i] = True


g1 = Graph()
g1.addEdge(1, 2)
g1.addEdge(1, 3)
g1.addEdge(1, 5)
g1.addEdge(2, 1)
g1.addEdge(2, 4)
g1.addEdge(3, 1)
g1.addEdge(3, 5)
g1.addEdge(4, 2)
g1.addEdge(5, 1)
g1.addEdge(5, 3)
g1.addEdge(4, 6)
g1.addEdge(6, 4)
g1.showEdge()
g1.BFS(6)
