# -*- encoding: utf-8 -*-
"""
There is a game of stone merging. At the beginning, there were n piles of stones arranged in a row.
The goal was to combine all the stones into a pile. The consolidation rules are as follows:
1. Each time you can merge consecutive x piles, left <= x <= right.
2. The cost of each merger is the sum of the weight of the combined x piles.
Find the minimum merge cost, if you cannot complete the merge return 0.

Example
Given n = 4, left = 3, right = 3, weight = [1,2,3,4], return 0.
Explanation:
Unable to complete the merge.

Given n = 3, left = 2, right = 3, weight = [1,2,3], return 6.
Explanation:
Merge 1,2,3, the merger cost is 1 + 2 + 3 = 6.

Notice
1 <= n <= 100，2 <= left <= right <= n
1 <= weight[i] <= 1000

Solution: dp(i, j, k)代表合并[i, j]区间为k堆所需要最小代价
sum(i, j)代表sum(weight[i...j])
dp(i, j, k) = min(dp(i, t, k-1) + dp(t+1, j, 1))
dp(i, j, 1) = min(dp(i, j, t)) + sum(i, j) where left <= t <= right
"""

class Solution:
    """
    @param n: The number of stones
    @param left: The minimum length to merge stones
    @param right: The maximum length to merge stones
    @param weight: The weight array
    @return: Return the minimum cost
    """
    def getMinimumCost(self, n, left, right, weight):
        pre = [0 for i in range(n + 1)]
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + weight[i - 1]

        dp = [ [ [ float('inf') for _ in range(n+1)] for _ in range(n+1) ] for _ in range(n+1) ]
        for i in range(1, n + 1):
            dp[i][i][1] = 0

        # The final dp[1][n][1] relies on smaller interval, so start from smaller len
        for len in range(1, n + 1):
            for i in range(1, n - (len-1) + 1):
                j = i + len - 1
                # cannot optimized to range(max(2, left), min(len+1, right+1)), dp[i][j][k] is also used in calculating larger [i, j]
                for k in range(2, len + 1):
                    for t in range(i, j):
                        dp[i][j][k] = min(dp[i][j][k], dp[i][t][k - 1] + dp[t + 1][j][1])

                for k in range(left, right + 1):
                    dp[i][j][1] = min(dp[i][j][1], dp[i][j][k] + pre[j] - pre[i - 1])

        return dp[1][n][1] if dp[1][n][1] != float('inf') else 0

print(Solution().getMinimumCost(4, 3, 3, [1,2,3,4])) # 0
print(Solution().getMinimumCost(3, 2, 3, [1,2,3])) # 6