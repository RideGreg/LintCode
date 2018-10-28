"""
795. 4-Way Unique Paths
A robot is located at the top-left corner of a m x n grid.

The robot can move any direction at any point in time, but every grid can only be up to once.
The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?

Example
Given m = 2 and n = 3, return 4.
Given m = 3 and n = 3, return 12.
"""

class Solution:
    """
    @param m: the row
    @param n: the column
    @return: the possible unique paths
    """
    def uniquePaths(self, m, n):
        def dfs(x, y):
            if x == m-1 and y == n-1:
                self.ans += 1
                return

            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0<=nx<m and 0<=ny<n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    dfs(nx, ny)
                    visited[nx][ny] = False

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = [[False]*n for _ in xrange(m)]
        visited[0][0]= True
        self.ans = 0
        dfs(0, 0)
        return self.ans

print(Solution().uniquePaths(2, 3)) # 4
print(Solution().uniquePaths(3, 3)) # 12