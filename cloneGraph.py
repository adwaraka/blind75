# Definition for a Graph Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# Clone the graph
class CloneGraph:
    def cloneGraph(self, node):
        if node is None:
            return None

        queue = [node]  # for the BFS
        # clone will be the copied version of the graph
        clones = dict()
        clones[node.val] = Node(node.val, [])

        while queue:
            current = queue.pop(0)
            currentClone = clones[current.val]
            for neighbor in current.neighbors:
                # if neighbor has not been cloned
                if neighbor.val not in clones:
                    clones[neighbor.val] = Node(neighbor.val, [])
                    queue.append(neighbor)

                # create the graph; THAT particular node and it's 
                # connected neighbors will be created.
                currentClone.neighbors.append(clones[neighbor.val])
        return clones[node.val]


n1 = Node('a', [])
n2 = Node('b', [])
n3 = Node('c', [])
n4 = Node('d', [])
n5 = Node('e', [])
n6 = Node('x', [])
n1.neighbors.append(n2)
n1.neighbors.append(n3)
n2.neighbors.append(n4)
n2.neighbors.append(n5)
n1.neighbors.append(n6)
cloneGraph = CloneGraph()
cloned = cloneGraph.cloneGraph(n1)
print(cloned.neighbors)  # for printing n1 neighbors
print(cloned.val)  # n1 value
