https://www.geeksforgeeks.org/detect-cycle-in-a-graph/

from collections import defaultdict


class Solution:
    """
    @param start: The start points set
    @param end: The end points set
    @return: Return if the graph is cyclic
    """
    def isCyclicGraph(self, start, end):
        def dfs(node, visited, stack):
            visited[node] = True
            stack.add(node)
            for ne in graph[node]:
                if ne in stack:
                    return True
                if not visited[ne] and dfs(ne, visited, stack):
                    return True
            stack.remove(node)
            return False

        # construct graph.
        vertex = 0
        graph = defaultdict(list)
        for u, v in zip(start, end):
            graph[u].append(v)
            vertex = max(vertex, u, v)
        vertex += 1

        visited, stack = [False] * vertex, set()
        for node in xrange(vertex):
            if not visited[node] and dfs(node, visited, stack):
                return True
        return False

print Solution().isCyclicGraph([1,3], [2,1])
print Solution().isCyclicGraph([1,2,3], [2,3,1])