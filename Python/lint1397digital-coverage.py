class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param intervals: The intervals
    @return: The answer
    """
    def digitalCoverage(self, intervals):
        mstart, mend = 0, 0
        for i in intervals:
            mstart = max(mstart, i.start)
            mend = max(mend, i.end)
        t = [0]*(max(mstart, mend)+2)
        for i in intervals:
            t[i.start] += 1
            t[i.end+1] -= 1
        mm, ans, localMax = -1, -1, 0
        for i, tt in enumerate(t):
            localMax += tt
            if localMax > mm:
                mm = localMax
                ans = i
        return ans

print Solution().digitalCoverage([Interval(1,7), Interval(2,8)])
print Solution().digitalCoverage([Interval(1,3), Interval(2,3), Interval(3,4)])

