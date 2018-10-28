# -*- encoding: utf-8 -*-
"""
There is a circle, divided into n sectors. All the sectors are colored with some of m colors.
The colors of adjacent sectors cannot be the same. Find the total number of plans.
- Do not consider symmetry.
- Since this number may be large, you only need to return the solution number mod 1e9 + 7.
1 <= n, m <= 10**5

Example
Given n = 2, m = 3, return 6.
Explanation:
One circle is divided into two sectors. There are six kinds of schemes for coloring in three colors:
black, red, black and white, white and red, white and black, red and white, and red and black.

Given n = 3, m = 2, return 0.
Explanation:
A circle is divided into 3 sectors and colored with 2 colors. No matter how it is colored, there is no guarantee
that the adjacent colors are different.

Solution: 设 f[i] 代表 i 个扇形，用 m 种颜色给每个扇形染色的答案。
let f[i] is the # of plans for i sectors and m colors.
f[1] = m, f[2] = m * (m - 1), f[3] = m * (m - 1) * (m - 2),
for i >= 4, f[i] = f[i - 1] * (m - 2)  # adjacent 2 sectors: different colors
                 + f[i - 2] * (m - 1)  # adjacent 2 sectors: same colors

return f[n]
Time complexity O(n)
"""

class Solution:
    """
    @param n: the number of sectors
    @param m: the number of colors
    @return: The total number of plans.
    """
    def getCount(self, n, m):
        if n == 1: return m
        elif n == 2: return m * (m-1)
        elif n == 3: return m * (m-1) * (m-2)
        else:
            prev, prev2 = m * (m-1) * (m-2), m * (m-1)
            for _ in xrange(4, n+1):
                prev, prev2 = (prev * (m-2) + prev2 * (m-1)) % (10**9+7), prev
            return prev

print(Solution().getCount(2, 3)) # 6