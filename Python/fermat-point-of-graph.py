# -*- encoding: utf-8 -*-

"""
There is a non acyclic connected graph. Each edge is described by two vertices x[i] and y[i],
and the length of each edge is described by d[i].
Find a point p such that the sum of distances from point p to other points is the smallest.
If there is more than one such point p, return the smallest number.

Example
Given x = [1], y = [2], d = [3], return 1.
Explanation:
The distance from other points to 1 is 3, the distance from other points to 2 is 3, and the number of 1 is smaller.

Given x = [1,2,2], y = [2,3,4], d = [1,1,1], return 2.
Explanation:
The distance from other points to 1 is 5, the distance from other points to 2 is 3, the distance from other points to 3 is 5, and the distance from other points to 4 is 5.

Notice: 2 <= n, d[i] <= 10^5, 1 <= x[i], y[i] <= n

Solution: 树形DP: DP 先算子，再算父，用好状态转移方程或recursion
dp[i] 代表以 i 为根的子树中的结点到 i 结点的距离和，dp[i] = sum(dp[j] + Size[j] * d(i, j)) where j is each neighbor
Size[i] 代表以 i 为根的子树的所有结点的个数，Size[i] = sum(Size[j]) + 1。
"""

class Solution:
    """
    @param x: The end points set of edges
    @param y: The end points set of edges
    @param d: The length of edges
    @return: Return the index of the fermat point
    """
    def getFermatPoint(self, x, y, d):
        # for the tree rooted with first node, build dp and Size for all nodes in the tree.
        def build_dfs(x, parent):
            Size[x], dp[x] = 1, 0
            for nei, weight in graph[x].iteritems():
                if (nei == parent):
                    continue
                build_dfs(nei, x)
                Size[x] += Size[nei]
                dp[x] += dp[nei] + weight * Size[nei]

        # moving from root to leaves, compare and get the node with minimal total distance to all other nodes.
        def solve_dfs(x, parent, Sum, n):
            for nei, weight in graph[x].iteritems():
                if (nei == parent):
                    continue
                nextSum = dp[nei] + (Sum - dp[nei] - Size[nei] * weight) + (n - Size[nei]) * weight
                if (nextSum < self.minSum or (nextSum == self.minSum and nei < self.idx)):
                    self.minSum = nextSum
                    self.idx = nei
                solve_dfs(nei, x, nextSum, n)

        # build graph. This is a non-acyclic graph, each edge adds one node, so total node # = total edge # + 1
        n = len(x) + 1
        graph = [{} for _ in xrange(n+1)] # one dummy node '0'
        for i in xrange(len(d)):
            graph[x[i]][y[i]] = d[i]
            graph[y[i]][x[i]] = d[i]

        dp, Size = [0] * (n+1), [0] * (n+1)
        build_dfs(1, 0)

        self.minSum, self.idx = dp[1], 1
        solve_dfs(1, 0, dp[1], n)
        return self.idx

    # TLE: use Dijkstra to get each node to all other nodes' distance. find the node with minimal total distance.
    def getFermatPoint_dijkstra(self, x, y, d):
        import heapq

        n = max(max(x), max(y))
        graph = [{} for _ in xrange(n+1)]
        for i in xrange(len(d)):
            graph[x[i]][y[i]] = d[i]
            graph[y[i]][x[i]] = d[i]

        def dijkstra_DG(i, N):
            pq = [(0, i)]  # (dist, node) dist is the key for ordering.
            dist = [float('inf')] * N
            dist[i] = 0
            dist[0] = 0 # dummy node

            while pq:
                d, node = heapq.heappop(pq)
                # Each node is only visited once.
                if d > dist[node]: continue

                for nei, weight in graph[node].iteritems():
                    # d2 is the total distance to reach 'nei' (neighbor) node.
                    d2 = d + weight
                    if d2 < dist[nei]:
                        heapq.heappush(pq, (d2, nei))
                        dist[nei] = d2

            print dist
            return sum(dist)

        minDist, ans = float('inf'), None
        for i in xrange(1, n+1):
            curDist = dijkstra_DG(i, n+1)
            if curDist < minDist:
                minDist = curDist
                ans = i
        return ans

print(Solution().getFermatPoint([1], [2], [3])) # 1
print(Solution().getFermatPoint([1,2,2], [2,3,4], [1,1,1])) # 2