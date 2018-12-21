# -*- encoding: utf-8 -*-

# There are a city's N bus information, route[i] stores the bus stop through which the i-th bus passes,
# find the minimum number of transfers from station A to station B. If you can't get to B from A, return -1.
# 1 <= N <= 100, 2 <= |route[i]| <= 100, 0 <= route[i][j] <= 2^31 - 1

# Solution: bfs 建图node is stop，但是next step 不只一个stop，而是所经过routes上的所有stops。 注意剪枝。

class Solution:
    """
    @param N: int The total number of buses
    @param route: array, The route of buses
    @param A: Start bus station
    @param B: End bus station
    @return: Return the minimum transfer number
    """
    def getMinTransferNumber(self, N, route, A, B):
        import collections
        routeMap = collections.defaultdict(set)
        for i in range(N):
            for stop in route[i]:
                routeMap[stop].add(i)
        ans = 0
        if A == B: return ans

        q = collections.deque([A])
        usedStop, usedRoute = set([A]), set()
        while q:
            ans += 1
            size = len(q)
            for _ in range(size):
                cur = q.popleft()

                for r in routeMap[cur]:
                    if r not in usedRoute:
                        usedRoute.add(r)
                        if r in routeMap[B]:
                            return ans

                        for ss in route[r]:
                            if ss not in usedStop:
                                usedStop.add(ss)
                                q.append(ss)
        return -1

print(Solution().getMinTransferNumber(2, [[1, 2, 3, 4], [3, 5, 6, 7]], 1, 4))
print(Solution().getMinTransferNumber(2, [[1, 2, 3, 4], [3, 5, 6, 7]], 1, 7))
