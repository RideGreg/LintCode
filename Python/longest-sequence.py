'''
Given an array a containing n positive integers, you can arbitrarily select a number of numbers to form an arithmetic progression, what is the maximum length of the arithmetic progression that can be composed?

Given a = [1,2,5,9,10], return 3 (because 1,5,9).
Given a = [1,3], return 2.
'''

class Solution:
    """
    @param a: The array a
    @return: Return the maximum length
    """
    def getAnswer(self, a):
        # time n^2, n is length of a
        if len(a) < 3: return len(a)

        import collections
        a.sort()
        index = {x:i for i, x in enumerate(a)}
        longest = collections.defaultdict(lambda: 2)
        ans = 2
        for k in xrange(len(a)):
            for j in xrange(k):
                i = index.get(a[j]*2-a[k], None)
                if i is not None and i < j:
                    longest[(j,k)] = longest[(i,j)] + 1
                    ans = max(ans, longest[(j,k)])
        return ans

    def getAnswer_hash(self, a):
        # time n^2*m, n is length of a, m is length of longest arithmetic progression
        if len(a) < 3: return len(a)

        # need to sort, otherwise [3, 5, 1, 7] can find 3->5->7 only
        a.sort()
        S, ans = set(a), 2
        for i in xrange(len(a)):
            for j in xrange(i+1, len(a)):
                x, y, l = a[i], a[j], 2
                while 2*y-x in S:
                    x, y, l = y, 2*y-x, l+1
                ans = max(ans, l)
                if ans == len(a):
                    return ans
        return ans

print(Solution().getAnswer([3,5,1,7])) #4
print(Solution().getAnswer([321,506,777,645,779,206,885,211,414,47,133,385,650,863,904,706,607,251,568])) #3
print(Solution().getAnswer([1,2,5,9,10])) #3
print(Solution().getAnswer([1,3])) #2