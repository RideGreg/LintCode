# Given a n point on the two-dimensional coordinate system, output the maximum area of the rectangle that consisting of four points. If it cannot form a rectangle, output 0
#
# n <= 1000
# 0 <= x,y <= 1000
# each side of the rectangle is required to be perpendicular to the X or Y axis


class Solution(object):
    # iterate all possible diagonal point pairs
    def getMaximum(self, a):
        S = set(map(tuple, a))
        ans = 0
        for j in range(1, len(a)):
            for i in range(j):
                p1, p2 = a[i], a[j]
                if p1[0] != p2[0] and p1[1] != p2[1] and (p1[0], p2[1]) in S \
                    and (p2[0], p1[1]) in S:
                    ans = max(ans, abs(p1[0] - p2[0]) * abs(p1[1] - p2[1]))
        return ans

    # Solution: use a couple of dicts. Dict 1 to store all Ys for a given X key; dict 2 to store
    # all Xs for a given Y pair key.
    def getMaximum_sortByColumn(self, a):
        import collections
        columns = collections.defaultdict(list)
        firstx, ans = {}, 0

        points = list(set(map(tuple, a)))  # remove duplicates
        for x, y in points:
            columns[x].append(y)

        for x in sorted(columns): # sorted(dict) is a sorted list of keys. no values
            ys = columns[x]
            ys.sort()
            for j in range(1, len(ys)):
                for i in range(j):
                    y1, y2 = ys[i], ys[j]
                    if (y1, y2) not in firstx:
                        firstx[y1, y2] = x
                    else:
                        ans = max(ans, (x - firstx[y1, y2]) * (y2-y1))
        return ans
    '''
    # this solution is for any rectangle NOT necessarily perpendicular to X/Y axis
    def getMaximum(self, a):
        import collections
        lookup = collections.defaultdict(list)
        ans = 0

        points = list(set(map(tuple, a))) # remove duplicates
        for j, p2 in enumerate(points):
            for i in xrange(j):
                p1 = points[i]
                d2 = (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2
                if p2[0] == p1[0]:
                    r = 's'
                else:
                    r = float(p2[1] - p1[1]) / (p2[0] - p1[0])
                if p1[0]<p2[0] or (p1[0]==p2[0] and p1[1]<p2[1]):
                    lookup[(r, d2)].append((p1, p2))
                else:
                    lookup[(r, d2)].append((p2, p1))

        for k, ps in lookup.iteritems():
            if len(ps) >= 2:
                for j, pair2 in enumerate(ps):
                    for i in xrange(j):
                        p1, p2 = pair2
                        p3, p4 = ps[i]
                        if p2 == p3 or p4 == p1: continue

                        flag = False
                        if k[0] == 0:
                            if p1[0]==p3[0] and p2[0]==p4[0]: flag = True
                        elif k[0]=='s':
                            if p1[1]==p3[1] and p2[1]==p4[1]: flag = True
                        else:
                             if p3[0] != p1[0] and abs(-1-float(p3[1] - p1[1]) / (p3[0] - p1[0]) * k[0]) < 1e-5: flag = True
                        if flag:
                            dd2 = (p3[0] - p1[0])**2 + (p3[1] - p1[1])**2
                            ans = max(ans, (k[1] * dd2)**0.5)
                            if int(ans) == ans:
                                ans = int(ans)
        return ans if ans < float('inf') else 0
    '''

print(Solution().getMaximum([[1,1],[1,2],[2,1],[2,2],[2,3],[3,2],[3,1]])) # 2
# The four points selected are: [1,1], [1,2], [3,1], [3,2]

print(Solution().getMaximum([[1,1],[1,2],[2,2],[2,3],[3,3],[3,4],[4,4]])) # 0