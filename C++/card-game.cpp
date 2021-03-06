class Solution {
public:
    /**
     * @param n: The number of cards
     * @param totalProfit: The totalProfit
     * @param totalCost: The totalCost
     * @param a: The profit of cards
     * @param b: The cost of cards
     * @return: Return the number of legal plan
     */
    int numOfPlan(int n, int totalProfit, int totalCost, vector<int> &a, vector<int> &b) {
        // Write your code here
        int dp[110][110];
        int mod = 1e9 + 7;
        
        memset(dp, 0, sizeof(dp));
        dp[0][0] = 1;
        for (int i = 0; i < n; i++) {
            for (int p = totalProfit + 1; p >= 0; p--) {
                for (int c = totalCost + 1; c >= 0; c--) {
                    int now_p = min(totalProfit + 1, p + a[i]);
                    int now_c = min(totalCost + 1, c + b[i]);
                    dp[now_p][now_c] = (dp[now_p][now_c] + dp[p][c]) % mod;
                }   
            }
        }
        
        int ans = 0;
        for (int i = 0; i < totalCost; i++) {
            ans = (ans + dp[totalProfit + 1][i]) % mod;
        }
        return ans;
        
    }
};
