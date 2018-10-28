public class Solution {
    /**
     * @param n: The number of stones
     * @param left: The minimum length to merge stones
     * @param right: The maximum length to merge stones
     * @param weight: The weight array
     * @return: Return the minimum cost
     */
    public int getMinimumCost(int n, int left, int right, int[] weight) {
        // Write your code here
        int [] pre = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            pre[i] = pre[i - 1] + weight[i - 1];
        }
        int[][][]dp = new int[205][205][205];
        int INF = 1000000000;
        for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= n; j++) {
                for(int k = 1; k <= n; k++) {
                    dp[i][j][k] = INF;
                }
            }
        }
        for (int i = 1; i <= n; i++) {
            dp[i][i][1] = 0;
        }
        for (int len = 1; len <= n; len++) {
            for (int i = 1; i + len - 1 <= n; i++) {
                int j = i + len - 1;
                for (int k = 2; k <= len; k++) {
                    for (int t = i; t + 1 <= j; t++) {
                        dp[i][j][k] = Math.min(dp[i][j][k], dp[i][t][k - 1] + dp[t + 1][j][1]);
                    }
                }
                for (int k = left; k <= right; k++) {
                    dp[i][j][1] = Math.min(dp[i][j][1], dp[i][j][k] + pre[j] - pre[i - 1]);   
                }
            }
        }
        if (dp[1][n][1] >= INF) {
            return 0;
        }
        return dp[1][n][1];
    }
}
