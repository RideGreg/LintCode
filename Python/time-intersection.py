class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param seqA: the list of intervals
    @param seqB: the list of intervals
    @return: the time periods
    """
    def timeIntersection(self, seqA, seqB):
        ans = []
        for a in seqA:
            for b in seqB:
                if a.start >= b.end or b.start >= a.end:
                    continue
                ans.append(Interval(max(a.start, b.start), min(a.end, b.end)))
        return ans

print Solution().timeIntersection([Interval(1,2), Interval(5,100)], [Interval(1,6)])
print Solution().timeIntersection([Interval(1,2), Interval(10,15)], [Interval(3,5), Interval(7,9)])