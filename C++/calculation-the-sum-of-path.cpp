class Solution{
public:
    /**
     * @param l: The length of the matrix
     * @param w: The width of the matrix
     * @param points: three points
     * @return: The sum of the paths sum
     */
    long long dp[2006][2006];
    const long long mod = 1000000007;
    long long solve(long long n, long long m)    {
        long long i, j;
        memset(dp, 0, sizeof(dp));
        for (i = 1; i <= n; i++) {
            dp[i][1] = 1;
        }
        for (i = 1; i <= m; i++) {
            dp[1][i] = 1;
        }
        for (i = 2; i <= n; i++)
            for (j = 2; j <= m; j++) {
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % mod;
            }
        return dp[n][m];
    }
    int calculationTheSumOfPath(int l, int w, vector<Point> &points) {
        // Write your code here
        long long n, m;
        long long i, ans;
        sort(points.begin(), points.end(), [](const Point & a, const Point & b) {
            if (a.x != b.x) {
                return a.x < b.x;
            }
            else {
                return a.y < b.y;
            }
        });

        // SHOULD ONLY CALCULATE DP MATRIX ONCE - MING
        ans = solve(points[0].x, points[0].y) % mod;
        ans = ans * solve(points[ 1].x - points[0].x + 1, points[1].y - points[0].y + 1) % mod;
        ans = ans * solve(points[ 2].x - points[1].x + 1, points[2].y - points[1].y + 1) % mod;
        ans = ans * solve(l - points[2].x + 1, w - points[2].y + 1) % mod;
        return ans;
    }
};
