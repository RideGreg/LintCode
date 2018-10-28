"""
1447. Calculation The Sum Of Path

Enter the length l and width w of a matrix, and three points (1 based index) that must pass. Ask how many ways you can go
from the upper left corner to the lower right corner (every step, you can only go right or go down).
The input is guaranteed that there is at least one legal path. You only need to return the solution number mod 1000000007.

Example
Given l=4, w=4. The three mandatory points are [1,1],[2,2],[3,3]. Return 8.
Explanation:
[1,1]->[1,2]->[2,2]->[2,3]->[3,3]->[3,4]->[4,4]
[1,1]->[1,2]->[2,2]->[2,3]->[3,3]->[4,3]->[4,4]
[1,1]->[1,2]->[2,2]->[3,2]->[3,3]->[3,4]->[4,4]
[1,1]->[1,2]->[2,2]->[3,2]->[3,3]->[4,3]->[4,4]
[1,1]->[2,1]->[2,2]->[2,3]->[3,3]->[3,4]->[4,4]
[1,1]->[2,1]->[2,2]->[2,3]->[3,3]->[4,3]->[4,4]
[1,1]->[2,1]->[2,2]->[3,2]->[3,3]->[3,4]->[4,4]
[1,1]->[2,1]->[2,2]->[3,2]->[3,3]->[4,3]->[4,4]
The sum is 8.

Given l=1, w=5. The three points are [1,2],[1,3],[1,4]. Return 1.
Explanation:
[1,1]->[1,2]->[1,3]->[1,4]->[1,5]
The sum is 1.

Notice 1 <= l, w <= 2000

Solution: divide the problem into 4 intervals, each can be solved by dynamic programming.
"""

class Solution:
    """
    @param l: The length of the matrix
    @param w: The width of the matrix
    @param points: three points
    @return: The sum of the paths sum
    """
    def calculationTheSumOfPath(self, l, w, points):
        # sort and validate input points
        # key is a function that returns a tuple: https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes
        points.sort(key=lambda i:(i[0], i[1]))
        if points[1][1] > points[0][1] or points[2][1] > points[1][1]:
            return 0

        # calculate length/width of 4 intervals
        points.insert(0, [1, 1])
        points.append([l, w])
        width, length = [], []
        for i in xrange(1, len(points)):
            length.append(points[i][0] - points[i-1][0])
            width.append(points[i][1] - points[i-1][1])

        # same to Leetcode #62 Unique Paths
        dp = [ [0]*(max(length)+1) for _ in xrange(max(width)+1) ]
        dp[0] = [1] * (max(length)+1)
        for i in xrange(1, len(dp)):
            dp[i][0] = 1
            for j in xrange(1, len(dp[0])):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        ans = 1
        for i in xrange(len(length)):
            ans *= dp[width[i]][length[i]]
            ans %= 10**9+7
        return ans

print(Solution().calculationTheSumOfPath(4, 4, [[1,1],[2,2],[3,3]])) # 8
print(Solution().calculationTheSumOfPath(1, 5, [[1,2],[1,3],[1,4]])) # 1