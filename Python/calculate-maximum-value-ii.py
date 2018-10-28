# -*- encoding: utf-8 -*-

"""
741. Calculate Maximum Value II
Given a string of numbers, write a function to find the maximum value from the string,
you can add a + or * sign between any two numbers，It's different with Calculate Maximum Value,
You can insert parentheses anywhere.

Example
Given str = 01231, return 12
(0 + 1 + 2) * (3 + 1) = 12 we get the maximum value 12

Given str = 891, return 80
As 8 * (9 + 1) = 80, so 80 is maximum.

Solution: Interval DP
定义dp[i][j]: 以[i,j]位置为区间的插入符号进行运算后所得最大值。
递推公式： dp[i][j] = max(dp[i][k]*dp[k+1][j], dp[i][k]+dp[k+1][j]) k in [i, j-1]
"""


class Solution:
    """
    @param str: a string of numbers
    @return: the maximum value
    """
    def maxValue(self, str):
        def calc(a, b):
            return max(a+b, a*b)

        sz = len(str)
        dp = [[-1]*sz for _ in xrange(sz)]
        for i in reversed(xrange(sz)):
            for j in xrange(i, sz):
                if i == j:
                    dp[i][i] = int(str[i])
                else:
                    for k in xrange(i,j):
                        dp[i][j] = max(dp[i][j], calc(dp[i][k], dp[k+1][j]))
        return dp[0][-1]

print Solution().maxValue('891')
print Solution().maxValue('01231')

