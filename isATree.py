# determine if a graph is a tree or not
# - graph does not have a node that is unreachable
# - graph does not revisit a node

from collections import defaultdict
 
class Graph():
 
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph  = defaultdict(list)

    def addEdge(self, vertex1, vertex2):
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def isCyclic(self, current, parent, visited):
        # the current node has been visited
        visited[current] = True

        for connectedNode in self.graph[current]:
            # if its not been visited
            if visited[connectedNode] == False:
                if self.isCyclic(connectedNode, current, visited):
                    return True

            # so node has been visited; check if
            # connected node should not be the parent!
            elif connectedNode != parent:
                return True

        return False

    def isATree(self):
        if self.vertices is None:  # empty tree
            return True

        # check if all vertices are visited
        visited = [False]*self.vertices

        # Check if cyclic or not
        # 0 is child, -1 is parent as in non-existent
        if self.isCyclic(0, -1, visited):
            return False

        # check if every node has been visited
        for val in visited:
            if val is False:
                return False

        return True


# Driver program to test above functions
g1 = Graph(5)
g1.addEdge(0, 1)
g1.addEdge(1, 2)
g1.addEdge(2, 3)
g1.addEdge(3, 4)
g1.addEdge(4, 0)
print(g1.isATree())

g2 = Graph(6)
g2.addEdge(0, 1)
g2.addEdge(0, 2)
g2.addEdge(0, 3)
g2.addEdge(3, 4)
g2.addEdge(4, 5)
print(g2.isATree())

g3 = Graph(6)
g3.addEdge(0, 1)
g3.addEdge(0, 2)
g3.addEdge(3, 4)
g3.addEdge(4, 5)
print(g3.isATree())
