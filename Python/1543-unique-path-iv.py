# Give two integers to represent the height and width of the grid. The starting point is
# in the upper left corner and the ending point is in the upper right corner. You can go to
# the top right, right or bottom right. Find out the number of paths you can reach the end.
# And the result needs to mod 1000000007.

class Solution:
    """
    @param height: the given height
    @param width: the given width
    @return: the number of paths you can reach the end
    """
    def uniquePath(self, height, width):
        mod = 10**9+7
        dp = [[0]*height, [0]*height]
        dp[0][0] = 1
        for k in range(1, width):
            start = max(0, i-1)
            end = min(height,i+2)
            dp[k%2] = [sum(dp[(k-1)%2][start:end]) % mod for i in range(height)]
        return dp[(width-1)%2][0]

    def uniquePath2(self, height, width): # elements handled separately
        mod = 10**9+7
        dp = [[0]*height, [0]*height]
        dp[0][0] = 1
        for k in range(1, width):
            dp[k % 2][0] = dp[(k-1)%2][0] + dp[(k-1)%2][1]
            for i in range(1, height-1):
                dp[k % 2][i] = sum(dp[(k - 1) % 2][i-1:i+2])
            dp[k % 2][height-1] = dp[(k-1)%2][height-2] + dp[(k-1)%2][height-1]
        return dp[(width-1)%2][0] % mod

print(Solution().uniquePath(3, 3)) # 2