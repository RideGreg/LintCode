# Given a List of intervals, the length of each interval is 1000, such as [500,1500], [2100,3100].Give a
# number arbitrarily and determine if the number belongs to any of the intervals.return True or False.

class Solution:
    """
    @param intervalList:
    @param number:
    @return: return True or False
    """
    def isInterval(self, intervalList, number):
        return "True" if any(it[0]<=number<=it[1] for it in intervalList) else "False"
        '''
        intervalList.sort()
        n = len(intervalList)
        l, r = 0, n-1
        while l <= r:
            m = l + (r-l) // 2
            if intervalList[m][0] <= number <= intervalList[m][1]:
                return "True"
            elif intervalList[m][0] > number:
                r = m - 1
            else:
                l = m + 1
        return "False"
        '''

print(Solution().isInterval([[100,1100],[1000,2000],[5500,6500]], 6000)) # "True"