'''
Given two Sparse Matrix A and B, return the result of AB.
You may assume that A's column number is equal to B's row number.

Example
A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
'''

class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        m, n, l = len(A), len(A[0]), len(B[0])
        ans = [[0] * l for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                for k in xrange(l):
                    if A[i][j] and B[j][k]:
                        ans[i][k] += A[i][j] * B[j][k]
        return ans

    def multiply_computeAll(self, A, B):
        ans = []
        for a in A:
            row = []
            for b in zip(*B):
                row.append(sum(x*y for x, y in zip(a, b)))
            ans.append(row)
        return ans

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

print(Solution().multiply(A, B))