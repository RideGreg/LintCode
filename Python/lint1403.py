class Solution:
    """
    @param x: The end points of edges set
    @param y: The end points of edges set
    @param d: The weight of points set
    @return: Return the maximum product
    """

    def getProduct(self, x, y, d):
        def dfs(s, cur):
            cur *= d[s - 1]
            if s not in edges:
                ans[0] = max(ans[0], cur % (10 ** 9 + 7))
                return
            for e in edges[s]:
                dfs(e, cur)

        import collections
        edges = collections.defaultdict(list)
        for s, e in zip(x, y):
            edges[s].append(e)
        ans = [float("-inf")]
        dfs(1, 1)
        return ans[0]

print Solution().getProduct([1,2,2], [2,3,4], [1,1,-1,2])