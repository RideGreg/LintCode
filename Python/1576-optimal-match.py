# Given a matrix size of n * m, 1 represents the position of the person, 2 represents the position of
# the bicycle and 0 represents the space. If the person is at (x1, y1) and the bicycle is at (x2, y2),
# the distance between them is |x1-x2|+|y1-y2|. And one person can only match one bicycle, find a way
# to minimize the total distance between people and bicycles, return the minimum distance.

# the number of bicycles is equal to the number of people

class Solution:
    """
    @param matrix: the matrix
    @return: the minimum distance
    """
    def optimalMatch(self, matrix):
        # find all people and bicycle
        people = []
        bicycle = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    people.append((i, j))
                elif matrix[i][j] == 2:
                    bicycle.append((i, j))

        # construct weights
        n = len(people)

        def dist(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

        weights = [[-dist(people[i], bicycle[j]) for j in range(n)] for i in range(n)]

        # hungarian init
        y_L, y_R, RL_link = [0]*n, [0]*n, [0]*n
        for L in range(n):
            y_L[L] = max(weights[L])

        # hungary
        def hungary(L, visited_L, visited_R):
            visited_L.add(L)
            for R in range(n):
                if R not in visited_R and y_L[L] + y_R[R] == weights[L][R]:
                    visited_R.add(R)
                    if (RL_link[R] == -1 or hungary(RL_link[R], visited_L, visited_R)):
                        RL_link[R] = L
                        return True
            return False

        # hungarian
        for i in range(n):
            while True:
                # find augmentation path
                visited_L = set()
                visited_R = set()
                if hungary(i, visited_L, visited_R):
                    break

                # update delta
                delta = float('inf')
                for L in range(n):
                    if L in visited_L:
                        for R in range(n):
                            if R not in visited_R:
                                delta = min(delta, y_L[L] + y_R[R] - weights[L][R])
                if delta == float('inf'):
                    return -1

                for j in range(n):
                    if j in visited_L:
                        y_L[j] -= delta
                    if j in visited_R:
                        y_R[j] += delta

        result = 0
        for i in range(n):
            result -= weights[RL_link[i]][i]
        return result

print(Solution().optimalMatch([[1,1,1],[2,2,2]])) # 3