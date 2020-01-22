class Solution:
    """
    @param matrix : the martix
    @return: the distance of grid to the police
    """
    def policeDistance(self, matrix):
        m, n = len(matrix), len(matrix[0])
        police = []

        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 1:
                    matrix[i][j] = 'x'
                    police.append((i,j))
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        import collections
        def getD(matrix, start):
            used = set()
            q = collections.deque([])
            q.append(start)
            used.add((start[0], start[1]))
            q.append('#')
            step = 1
            while q:
                cur = q.popleft()
                if cur == '#' and q:
                    q.append('#')
                    step += 1
                    continue
                x,y = cur[0], cur[1]
                for dx, dy in dirs:
                    nx, ny = x+dx, y+dy
                    if 0<=nx<len(matrix) and 0<=ny<len(matrix[0]) and (nx,ny) not in used:
                        if matrix[nx][ny] == 'x':
                            return step
                        elif matrix[nx][ny] != -1:
                            q.append((nx, ny))
                            used.add((nx, ny))
            return float('-inf')

        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 0:
                    matrix[i][j] = getD(matrix, (i,j))
        for i, j in police:
            matrix[i][j] = 0
        return matrix

print Solution().policeDistance([
    [-1,0,0,0,0,1,0,0,1,1],
    [1,1,-1,0,0,0,0,0,1,0],
    [-1,0,1,0,-1,0,0,0,1,0],
    [0,0,0,0,1,-1,1,1,1,-1],
    [0,0,-1,1,1,-1,1,0,1,0],
    [0,1,1,1,0,0,1,0,1,0],
    [0,0,0,0,0,1,1,-1,0,-1],
    [1,1,1,0,0,0,0,1,1,0],
    [1,-1,0,1,0,0,-1,0,0,0],
    [0,1,0,0,1,1,1,0,1,1]])
print Solution().policeDistance([
    [0, -1, 0],
    [0, 1, 1],
    [0, 0, 0]
])
print Solution().policeDistance([
    [0, -1, -1],
    [0, -1, 1],
    [0, 0, 0]
])



