"""
There is a multi-branch tree whose n nodes are rooted at 1. Find the number of connected subgraphs of this tree.
Since the middle part of the calculation and the answer may exceed the range of long, the answer is modulo 10000007.
(Connected subgraph: optional x points (1 <= x <= n), any two points can reach each other)

Example
Given start = [1], end = [2], return 3.
Explanation:
There are 3 connected subgraphs [1], [2], [1->2].

Given start = [1,1], end = [2,3], return 6.
Explanation:
There are 6 connected subgraphs [1], [2], [3], [1->2], [1->3], [1->2,1->3].

Given start = [1,1,2], end = [2,3,4], return 10.
Explanation:
There are 10 connected subgraphs [1], [2], [3], [4], [1->2], [1->3], [2->4], [1->2,1->3], [1->2,2->4], [1->3,1->2,2->4] .

Notice
1 <= |start|,|end|,n <= 10^5
1 <= start[i],end[i] <= n

Solution:
count代表以i结点为根的子树的包含i结点的连通子图个数 i.count = prod((j.count) + 1)
ans代表以i结点为根结点的子树的所有连通子图个数 i.ans = i.count + sum(j.ans)
时空复杂度O(n)
"""

class Solution:
    """
    @param start: The start of the edges set
    @param end: The end of the edges set
    @return: Return the subtree count
    """
    def getSubtreeCount(self, start, end):
        def dfs(x, parent):
            # count is the # of subtrees for tree with 'x' as root
            count = 1
            for nei in graph[x]:
                if nei != parent:
                    count *= (dfs(nei, x) + 1)
            self.ans += count
            return count

        mod = 10**7 + 7
        n = len(start) + 1
        graph = [[] for _ in xrange(n+1)]
        for i in xrange(len(start)):
            graph[start[i]].append(end[i])
            graph[end[i]].append(start[i])

        self.ans = 0
        dfs(1, 0)
        return self.ans % mod

print(Solution().getSubtreeCount([1], [2])) # 3
print(Solution().getSubtreeCount([1, 1], [2, 3])) # 6
print(Solution().getSubtreeCount([1,1,2], [2,3,4])) # 10

