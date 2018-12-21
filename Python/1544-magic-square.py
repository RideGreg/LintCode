# -*- encoding: utf-8 -*-

# Give a positive integer n and fill 1 to n * n into a matrix of n * n. Make the sum of each row,
# column, and diagonal of the matrix are equal to each other.

# https://www.zhihu.com/question/23531676
# use Strachey method to construct singly even 4k+2
# 幻方可分为三类：奇阶幻方4k+1/3、双偶阶幻方4k和单偶阶幻方4k+2

class Solution:
    """
    @param n: an integer
    @return: return the matrix
    """
    def magicSquare(self, n):
        if n % 2 == 0: return []

        ans = [[-1] * n for _ in range(n)]
        x, y = 0, (n-1) // 2
        for i in range(1, n*n+1):
            ans[x][y] = i
            nx, ny = x-1, y+1
            if nx < 0: nx = n-1
            if ny > n-1: ny = 0

            if ans[nx][ny] == -1:
                x, y = nx, ny
            else:
                x, y = x+1, y
        return ans

print(Solution().magicSquare(3))