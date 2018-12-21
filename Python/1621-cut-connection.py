# Given a lego matrix consists of 0 and 1, the first line is the roof. '1' means there is a lego.
# Remove one of '1', the same column of the '1' that is not connected to the roof will drop and need to be set to '0'.
# A lego is connected to the roof if one of its neighbours is connected to the roof(neighbours means the left, right and top legos).

class Solution(object):
    def removeOne(self, matrix, x, y):
        matrix[x][y] = 0
        for r in range(x, len(matrix)):
            if r == 0:  # other elems in top row not need update
                continue

            matrix[r] = [-1 * v for v in matrix[r]]  # marked as -1 for "previously connected" Legos

            # if an item has a top lego, mark it as "connected". The only exception is the given point
            # which is always 0 and not calculate from upper row
            for j in range(len(matrix[0])):
                if matrix[r-1][j] == 1 and matrix[r][j] == -1:
                    matrix[r][j] = 1
            if r == x:
                matrix[x][y] = 0

            # iterate from left to right, connect Legos
            for j in range(1, len(matrix[0])):
                if matrix[r][j-1] == 1 and matrix[r][j] == -1:
                    matrix[r][j] = 1

            # iterate from right to left, connect Legos
            for j in reversed(range(len(matrix[0])-1)):
                if matrix[r][j + 1] == 1 and matrix[r][j] == -1:
                    matrix[r][j] = 1

            # remove previously connected but no longer connected Legos
            matrix[r] = [0 if v == -1 else v for v in matrix[r]]

        return matrix

    # if we don't consider left/right as connected, just simply wipe out all the legos in the same column
    # following downward direction
    def removeOne_simpleProblem(self, matrix, x, y):
        for i in range(x, len(matrix)):
            if matrix[i][y] == 0:
                break
            matrix[i][y] = 0
        return matrix

print(Solution().removeOne([
         [1,1,1,1,1],
         [0,0,1,0,1],
         [0,0,1,0,1],
         [0,0,1,0,0]
         ], 1, 2))
# return[[1,1,1,1,1],
#        [0,0,0,0,1],
#        [0,0,0,0,1],
#        [0,0,0,0,0]
#        ]
print(Solution().removeOne([
         [1,1,1,1,1],
         [0,0,1,0,1],
         [0,0,1,1,1],
         [0,0,1,0,0]
         ], 1, 2))
# return[[1,1,1,1,1],
#        [0,0,0,0,1],
#        [0,0,1,1,1],
#        [0,0,1,0,0]
#        ]
print(Solution().removeOne([
         [1,1,1,1,1],
         [0,0,1,0,0],
         [0,1,1,0,0],
         [0,1,0,0,0]
         ], 2, 2))
# return[[1,1,1,1,1],
#        [0,0,1,0,0],
#        [0,0,0,0,0],
#        [0,0,0,0,0]
#        ]
print(Solution().removeOne([
         [1,1,1,1,1],
         [1,0,1,0,0],
         [1,1,1,0,0],
         [0,1,0,0,0]
         ], 2, 2))
# return[[1,1,1,1,1],
#        [1,0,1,0,0],
#        [1,1,0,0,0],
#        [0,1,0,0,0]
#        ]