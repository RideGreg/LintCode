public class Solution {
    /**
     * @param l: The length of the matrix
     * @param w: The width of the matrix
     * @param points: three points 
     * @return: The sum of the paths sum
     */
    public long calculationTheSumOfPath(int l, int w, Point[] points) {
        // Write your code here
        long[][] dp = new long[l][w];
        long mod = 1000000007;
        for (int i = 0; i < l; i++) {
            dp[i][0] = 1;
        }
        for (int j = 0; j < w; j++) {
            dp[0][j] = 1;
        }
        for (int i = 1; i < l; i++) {
            for (int j = 1; j < w; j++) {
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % mod;
            }
        }
        long ans = 0;
        Point a = points[0], b = points[1], c = points[2], t;
        if (a.x >= b.x && a.y >= b.y) {
            t = a;
            a = b;
            b = t;
        }
        if (a.x >= c.x && a.y >= c.y) {
            t = a;
            a = c;
            c = t;
        }
        if (b.x >= c.x && b.y >= c.y) {
            t = b;
            b = c;
            c = t;
        }
        ans = dp[a.x - 1][a.y - 1];
        ans = ans * dp[b.x - a.x][b.y - a.y] % mod;
        ans = ans * dp[c.x - b.x][c.y - b.y] % mod;
        ans = ans * dp[l - c.x][w - c.y] % mod;
        return ans;
    }
}
