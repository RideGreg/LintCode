# There are a group of boxes and a group of positions. Given two arrays representing the height of boxes and
# the height of positions. You can put the box in the position if the height of the box is not higher than
# the position. And only one box can be placed per position. You need to put the box in position in order
# and find out the maximum number of boxes you can put in.

# Solutoin: Interval Dynamic Programming

class Solution:
    """
    @param box: the boxes
    @param position: the positions
    @return:  the maximum number of boxes you can put in
    """
    def putBox(self, box, position):
        m, n = len(box), len(position)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if box[i-1] <= position[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]

print(Solution().putBox([4,2,3,1], [1,2,3,4])) # 3