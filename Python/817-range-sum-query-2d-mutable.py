# Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its
# upper left corner (row1, col1) and lower right corner (row2, col2).

# 1.The matrix is only modifiable by the update function.
# 2.You may assume the number of calls to update and sumRegion function is distributed evenly.
# 3.row1 <= row2 and col1 <= col2.

# a 2D bit indexed tree
# Time: ctor O(MNlogMlogN), update O(logMlogN), sumRegion O(logMlogN)
# original mx
# 3 1 1 4
# 5 6 3 2
# 1 2 1 1
# 4 1 1 1
#
# tree: node stores range: odd node only stores itself, even node stores a wide range
# 8: 1->8, 7: 7, 6: 5->6, 5: 5, 4: 1->4, 3: 3, 2: 1->2, 1: 1
# after set the first elem mx[0][0]
# 0 0 0 0 0
# 0 3 3 0 3
# 0 3 3 0 3
# 0 0 0 0 0
# 0 3 3 0 3
# In query: add nodes with last-set-bit gradually removed: 6 = node 6 + node 4; 5 = node 5 + node 4

class NumMatrix(object):
    def __init__(self, matrix):
        m, n = len(matrix), len(matrix[0])
        self.mx = [[0] * n for _ in range(m)]
        self.tree = [[0] * (n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        delta = val - self.mx[row][col]
        if delta == 0: return

        self.mx[row][col] = val

        r = row + 1
        while r <= len(self.mx):
            c = col + 1
            while c <= len(self.mx[0]):
                self.tree[r][c] += delta
                c += c & (-c)
            r += r & (-r)

    def sumRegion(self, row1, col1, row2, col2):
        def getSum(row, col):
            r, s = row+1, 0
            while r > 0:
                c = col + 1
                while c > 0:
                    s += self.tree[r][c]
                    c -= c & (-c)
                r -= r & (-r)
            return s

        return getSum(row2, col2) - getSum(row1-1, col2) - getSum(row2, col1-1) + getSum(row1-1, col1-1)


# Treat each row as a segment tree
# TLE Time: ctor O(MN), update O(logN), sumRegion O(MlogN)
class NumMatrix_segmentTree(object):
    def __init__(self, matrix):
        m, self.n = len(matrix), len(matrix[0])
        self.tree = [[0] * 2 * self.n for _ in range(m)]
        for i in range(m):
            self.tree[i][self.n:] = matrix[i]
            for j in reversed(range(1, self.n)):
                self.tree[i][j] = self.tree[i][2 * j] + self.tree[i][2 * j + 1]

    def update(self, row, col, val):
        c = col + self.n
        if self.tree[row][c] != val:
            self.tree[row][c] = val
            while c > 0:
                sibling = c - 1 if c % 2 else c + 1
                self.tree[row][c / 2] = self.tree[row][c] + self.tree[row][sibling]
                c /= 2

    def sumRegion(self, row1, col1, row2, col2):
        s = 0
        for i in range(row1, row2 + 1):
            c1, c2 = col1 + self.n, col2 + self.n
            while c1 <= c2:
                if c1 % 2:
                    s += self.tree[i][c1]
                    c1 += 1
                if c2 % 2 == 0:
                    s += self.tree[i][c2]
                    c2 -= 1
                c1 /= 2
                c2 /= 2
        return s

obj = NumMatrix([[3,1,1,4,2],[5,6,3,2,1],[1,2,1,1,5],[4,1,1,1,7],[1,1,3,1,5]])
print(obj.sumRegion(2, 1, 4, 3)) # 12 = 2+1+1 + 1+1+1 + 1+3+1
obj.update(3, 2, 2)
print(obj.sumRegion(2, 1, 4, 3)) # 13 = 2+1+1 + 1+2+1 + 1+3+1