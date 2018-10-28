"""
630. Knight Shortest Path II
Given a knight in a chessboard n * m (a binary matrix with 0 as empty and 1 as barrier). the knight initialze position
is (0, 0) and he wants to reach position (n - 1, m - 1), Knight can only be from left to right. Find the shortest path 
to the destination position, return the length of the route. Return -1 if knight can not reached.

Example
[[0,0,0,0],
 [0,0,0,0],
 [0,0,0,0]]

Return 3

[[0,0,0,0],
 [0,0,0,0],
 [0,1,0,0]]

Return -1

Clarification
If the knight is at (x, y), he can get to the following positions in one step:
(x + 1, y + 2)
(x - 1, y + 2)
(x + 2, y + 1)
(x - 2, y + 1)
"""

class Solution:
    """
    @param grid: a chessboard included 0 and 1
    @return: the shortest path
    """
    # BFS解法，按步搜索， 如果终点值为1，直接返回-1，否则从左向右搜索，已经访问过的点置为1.
    # queue 所需空间小于DP解法所需空间。
    def shortestPath2(self, grid):
        if not grid or grid[-1][-1] == 1: return -1

        m, n = len(grid), len(grid[0])
        delta = [(-2,1), (2,1), (-1,2), (1,2)]
        import collections
        q, step = collections.deque([(0,0)]), 0
        while q:
            size = len(q)
            step += 1
            for _ in xrange(size):
                x, y = q.popleft()
                for dx, dy in delta:
                    nx, ny = dx+x, dy+y
                    if nx == m-1 and ny == n-1:
                        return step
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != 1:
                        grid[nx][ny] = 1
                        q.append((nx, ny))
        return -1

    def shortestPath2_dp(self, grid):
        if not grid or grid[-1][-1] == 1: return -1

        m, n = len(grid), len(grid[0])
        dirs = [(-2,1), (2,1), (-1,2), (1,2)]
        dp = [[float('inf')]*n for _ in xrange(m)]
        dp[0][0] = 0
        for y in xrange(1, n):
            for x in xrange(m):
                if grid[x][y] == 0:
                    for dx, dy in dirs:
                        px, py = x-dx, y-dy
                        if 0<=px<m and 0<=py<n and dp[px][py] != float('inf'):
                            dp[x][y] = min(dp[x][y], dp[px][py]+1)
        return dp[-1][-1] if dp[-1][-1] != float('inf') else -1
