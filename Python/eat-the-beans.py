# -*- encoding: utf-8 -*-
"""
There are W white beans and R red beans in one bag. The first step: random touch a bean,
touch white beans to eat directly, touch red beans, put back.
The second step: random touch another bean, whether it is red or white, eat.
Then repeat the first and second steps to ask the probability of the last bean being white beans.

Example
Given W = 1,R = 1, return 0.25.
Explanation:
After the first step, the remaining 1 white beans and 1 red beans were 0.5, the remaining 0 white beans and 1 red beans were 0.5. After the second step the remaining 1 white beans and 0 red beans were 0.25, leaving 0 white beans and 1 red beans for 0.75.

Given W = 1,R = 0, return 1.
Explanation:
At the beginning, the last bean is white bean, that is, the probability is 1.

Notice: 0<= W,R<= 70

Solution: 2维dp。
根据当前状态有四种转移：先红后红，先红后白，先白后红，先白后白。
分别对应方程：dp[i][j-1]，dp[i-1][j]，dp[i-1][j-1]，dp[i-2][j]。
根据独立性概率可加，从状态dp[w][r]遍历。

时间复杂度O(n^2)
"""

class Solution:
    """
    @param w: The W
    @param r: The R
    @return: The answer
    """
    def eatTheBeans(self, w, r):
        if w == 0: return 0.0
        if r == 0: return 1.0

        # probability function
        def pww(w, r):
            return 1.0*w/(w+r)*(w-1)/(w+r-1)
        def pwr(w, r):
            return 1.0*w/(w+r)*r/(w+r-1)
        def prw(w, r):
            return 1.0*r/(w+r)*w/(w+r)
        def prr(w, r):
            return 1.0*r/(w+r)*r/(w+r)

        dp = [ [0] * (r+1) for _ in xrange(w+1) ]
        for i in xrange(1, w+1):
            dp[i][0] = 1.0
            for j in xrange(1, r+1):
                if i == 1:
                    dp[i][j] = prr(i,j) * dp[i][j-1]
                else:
                    dp[i][j] = pww(i,j)*dp[i-2][j] + pwr(i,j)*dp[i-1][j-1] \
                               + prw(i,j)*dp[i-1][j] + prr(i,j)*dp[i][j-1]
        return dp[w][r]

print(Solution().eatTheBeans(1,1)) # 0.25
print(Solution().eatTheBeans(1,0)) # 1.0