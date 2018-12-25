# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to
# adjacent numbers on the row below.

class Solution:
    def minimumTotal(self, triangle):
        n = len(triangle)
        dp = triangle[n-1]
        for i in xrange(n-2, -1, -1):
            for j in xrange(i+1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j+1])
        return dp[0]

print(Solution().minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
])) # 11
