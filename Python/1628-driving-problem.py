# -*- encoding=utf-8 -*-

# Time: O(n^2)
# Space: O(n)

# There is a road with a length L and a width W. There are some circular obstacles in the road. The radius is 1,
# there is a circular car with a radius of 2. Ask if the car can pass this road.
# You can think of the road as a rectangle on two-dimensional coordinates. The four points are (0,0), (0,W), (L,0), (L,W).
# Now you need to start from x=0 To x=L, contact with obstacles is not allowed, and all parts of the car
# are betweeny=0 and y=W, contact is not allowed.
#
# Example
# Given L=8,W=8, the obstacle coordinates are [[1,1],[6,6]]. Return yes.
# The center of the car can go from (0,5) to (2,5) to (5,2) to (8,2), so return yes.

# Give L=8, W=6, the obstacle coordinate is [[1,1]], and return no.
# Regardless of how you drive, the car will always be tangent to or intersect with obstacles, which is not allowed.

# Notice
# The coordinates of the obstacle can be floating point numbers
# The car can't drive out of the road
# The number of obstacles does not exceed 1,000.
# Obstacles can intersect or overlap

# Solution: union-find 连通性搜索
# 你可以想象成，如果障碍物之间不能通过小车（中心点距离小于等于36=(1+4+1)^2），那么就连通他们(union他们的index)。外加如果障碍物上方不能通过，
# 就union这个障碍物的index和一个特别的数（比如我把上方不能通过的index统一和p.length union）；障碍物下方不能通过同理，可以用p.length + 1去union。
# 结果就是找p.length 和 p.length + 1有没有形成一个union。如果是的话，就说明中间有一个或多个障碍物搭桥，并且他们之间不能过小车
# （外加上下都不能过，小车就卡住了）。如果不是的话，就说明小车畅通无阻（要么上面能过，要么下面能过）。

class Solution:
    """
    @param L: the length
    @param W: the width
    @param p:  the obstacle coordinates
    @return: yes or no
    """
    def drivingProblem(self, L, W, p):
        def find(i):
            if root[i] != i:
                root[i] = find(root[i])
            return root[i]

        def union(i, j):
            rooti, rootj = find(i), find(j)
            if rooti != rootj:
                root[rooti] = rootj

        n = len(p)
        root = range(n+2)
        for i in range(n):
            for j in range(i+1, n):
                dx = (p[i][0] - p[j][0]) ** 2
                dy = (p[i][1] - p[j][1]) ** 2
                if dx + dy <= (1+4+1)**2:
                    union(i, j)

            if p[i][1] <= 1+4: # connect to group representing bottom
                union(i, n)
            if W - p[i][1] <= 1+4:
                union(i, n+1)  # connect to group representing top

        return "no" if find(n) == find(n+1) else "yes"

print(Solution().drivingProblem(8, 8, [[1,1], [6,6]])) # "yes"
print(Solution().drivingProblem(8, 6, [[1,1]])) # "no"