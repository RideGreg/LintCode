# -*- encoding: utf-8 -*-

"""
631. Maximal Square II
Given a 2D binary matrix filled with 0's and 1's, find the largest square which diagonal is all 1 and others is 0.

Example
For example, given the following matrix:
1 0 1 0 0
1 0 0 1 0
1 1 0 0 1
1 0 0 1 0

Return 9

Notice
Only consider the main diagonal situation.
"""

class Solution:
    """
    @param matrix: a matrix of 0 an 1
    @return: an integer
    """
    # Time O(m * n), Space O(n). Maintain dp 2*n 2D lists, upZero 1D list向量, leftZero variable变量.
    def maxSquare2(self, matrix):
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n, [0]*n]
        upZero = [0]*n
        ans = 0
        for r in xrange(m):
            leftZero = 0
            for c in xrange(n):
                if matrix[r][c] == 1:
                    dp[r%2][c] = 1+min(dp[(r-1)%2][c-1], leftZero, upZero[c]) if r>0 and c>0 else 1
                    upZero[c] = 0
                    leftZero = 0
                else:
                    dp[r%2][c] = 0
                    upZero[c] += 1
                    leftZero += 1
                ans = max(ans, dp[r%2][c])
        return ans**2

    # O(m * n * max(m,n)): each node requires a 1D traverse
    def maxSquare2_worsePerf(self, matrix):
        def solve(r, c):
            if matrix[r][c] == 0:
                return 0

            ret = 1
            if c > 0:
                for i in xrange(dp[c-1]):
                    if matrix[r-i-1][c] == 1 or matrix[r][c-i-1] == 1:
                        break
                    ret += 1
            return ret

        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        dp = matrix[0]
        ans = max(dp)
        for r in xrange(1, m):
            for c in reversed(xrange(n)):
                dp[c] = solve(r, c)
                ans = max(ans, dp[c])
        return ans**2

print(Solution().maxSquare2([
[1, 0, 1, 0, 0],
[1, 0, 0, 1, 0],
[1, 1, 0, 0, 1],
[1, 0, 0, 1, 0]
]))

