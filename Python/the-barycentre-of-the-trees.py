# -*- encoding: utf-8 -*-

"""
For a multi-branch tree, if there is a node R with R as the root, and the largest sub-tree of all its sub-trees
has the least number of nodes, the node R is said to be the center of gravity of the tree.
Now give you a multi-branch tree with n nodes. Find the center of gravity of this tree.
If there are multiple centers of gravity, return the one with the lowest number.
x[i], y[i] represents the two points of the i-th edge.

Example
Given x = [1], y = [2], return 1.
Explanation:
Both 1 and 2 can be center of gravity, but the number of 1 is the smallest.

Given x = [1,2,2], y = [2,3,4], return 2.
Explanation:
2 is the center of gravity.

Notice: 2 <= n <= 10^5; 1 <= x[i], y[i] <= n

考点 树形 DP

题解
随意选择一个点作为树的根节点，比如 1 结点。
dp[i] 代表以 i 为根的子树的结点个数，dp[i] = sum(dp[j]) + 1。这里j 是 i 节点的所有子节点。
则以 i 为根的子树的最大结点个数为 max(max(dp[j]), n - dp[i])。
在 DFS 的过程中维护答案即可。
"""

class Solution:
    """
    @param x: The vertexes of the edges
    @param y: The vertexes of the edges
    @return: Return the index of barycentre
    """
    def getBarycentre(self, x, y):
        def dfs(x, parent, n):
            size[x] = 1
            maxSubtree = 0 # size of largest subtree of node 'x'
            for nei in graph[x]:
                if nei != parent:
                    dfs(nei, x, n)
                    size[x] += size[nei]
                    maxSubtree = max(maxSubtree, size[nei])
            maxSubtree = max(maxSubtree, n - size[x])

            if maxSubtree < self.minAns or (maxSubtree == self.minAns and x < self.idx):
                self.minAns = maxSubtree
                self.idx = x

        n = len(x) + 1
        graph = [[] for _ in xrange(n+1)] # one dummy node '0'
        for i in xrange(len(x)):
            graph[x[i]].append(y[i])
            graph[y[i]].append(x[i])

        size = [0] * (n+1)
        self.minAns, self.idx = n + 1, n + 1
        dfs(1, 0, n)
        return self.idx

print(Solution().getBarycentre([1,2,2], [2,3,4])) # 2
