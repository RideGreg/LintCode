# -*- encoding: utf-8 -*-

# Given a non-overlapping interval list which is sorted by start point.
# Insert a new interval into it, make sure the list is still in order and non-overlapping (merge intervals if necessary).

# 新建列表，不要in place scan & replace

# Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    """
    @param intervals: Sorted interval list.
    @param newInterval: new interval.
    @return: A new interval list.
    """
    # interval分为三部分，左边 end < newInterval.start, 右边 start > newInterval.end,
    # 中间是和newInterval纠缠不清的，把中间的interval合并，最后把三部分加起来
    def insert(self, intervals, newInterval): # USE THIS
        l, r, s, e = [], [], newInterval.start, newInterval.end
        for i in intervals:
            if i.end < s:
                l.append(i)
            elif i.start > e:
                r.append(i)
            else:
                s, e = min(s, i.start), max(e, i.end)
        return l + [Interval(s, e)] + r

        ''' # use tuple instead of Interval to run test
        l, r, s, e = [], [], newInterval[0], newInterval[1]
        for i in intervals:
            if i[1] < s:
                l.append(i)
            elif i[0] > e:
                r.append(i)
            else:
                s, e = min(s, i[0]), max(e, i[1])
        return l + [(s, e)] + r
        '''

    # ans is 1 list, need to insert in correct position
    def insert2(self, intervals, newInterval):
        ans, insertPos, s, e = [], 0, newInterval.start, newInterval.end
        for i in intervals:
            if i.end < s:
                ans.append(i)
                insertPos += 1
            elif i.start > e:
                ans.append(i)
            else:
                s, e = min(s, i.start), max(e, i.end)
        ans.insert(insertPos, Interval(s, e))
        return ans

print(Solution().insert([(1,2), (5,9)], (2,5))) # [(1,9)]
print(Solution().insert([(1,2), (5,9)], (3,4))) # [(1,2), (3,4), (5,9)]