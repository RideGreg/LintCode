# -*- encoding: utf-8 -*-

# Time: O(m*n)
# Space: O(m*n)

# Give a m * n board with a value of 0 or 1. At each step we can remove a point whose value is 1
# and there is another 1 in the same row or in the same column. Find a remove order which allows us
# to remove the most points, return the max number of points we can remove.

# 同行或同列有多个1则可删除 => 同行或同列合并多个1 => 合并问题用并查集
# 考察问题转换能力

class Solution:
    """
    @param mp: the board
    @return: the max number of points we can remove
    """
    def getAns(self, mp):
        def find(i):
            if root[i] != i:
                root[i] = find(root[i])
            return root[i]

        def union(i, j):
            ri, rj = find(i), find(j)
            if ri != rj:
                root[rj] = root[ri]
                self.ans += 1

        m, n = len(mp), len(mp[0])
        root = range(m*n)
        count = [0] * (m*n)
        rowLast, colLast, self.ans = {}, {}, 0

        for i in xrange(m):
            for j in xrange(n):
                if mp[i][j] == 1:
                    idx = n*i + j
                    count[idx] = 1

                    if i in rowLast:
                        union(n*i + rowLast[i], idx)
                    else:
                        rowLast[i] = j

                    if j in colLast:
                        union(n*colLast[j] + j, idx)
                    else:
                        colLast[j] = i
        return self.ans

print(Solution().getAns([[1,0,1],[1,0,0]])) # 2
print(Solution().getAns([[1,0],[1,0]])) # 1

