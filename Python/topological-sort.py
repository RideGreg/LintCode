# Topological Sorting: a linear traversal of a DAG so that for each directed edge uv, u comes before v in the ordering.
# Cannot apply if it is not a DAG.

# Idea: similar to DFS, but use a stack to store the vertices. Finally print stack in reversed order.

from collections import defaultdict

# Class to represent a graph
class Graph:
    def __init__(self, numOfV):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = numOfV  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive function used by topologicalSort
    def topologicalSortRec(self, v, visited, stack):
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortRec(i, visited, stack)

        # Push current vertex to stack which stores result
        stack.append(v)

    # The function to do Topological Sort. It uses recursive topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortRec(i, visited, stack)

        # Print contents of the stack
        print stack[::-1]


g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print "Following is a Topological Sort of the given graph"
g.topologicalSort() # [5, 4, 2, 3, 1, 0]