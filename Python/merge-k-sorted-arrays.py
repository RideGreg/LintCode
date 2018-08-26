'''
Time: O(Nlogk), Memory: O(k), Disk: O(N)

Given k sorted integer arrays, merge them into one sorted array.
Do it in O(N log k). N is the total number of integers. k is the number of arrays.

Example
Given
[
  [1, 3, 5, 7],
  [2, 4, 6],
  [0, 8, 9, 10, 11]
]
return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11].
'''

import heapq

class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays): # USE THIS
        k = len(arrays)
        h, ans = [], []
        for i in xrange(k):
            if arrays[i]:
                heapq.heappush(h, (arrays[i][0], i, 0))
        while h:
            v, i, pos = heapq.heappop(h)
            ans.append(v)
            if pos + 1 < len(arrays[i]):
                heapq.heappush(h, (arrays[i][pos+1], i, pos+1))

        return ans

    def mergekSortedArrays_mergeAPI(self, arrays):
        it = heapq.merge(*arrays)
        ans = []
        while 1:
            try:
                ans.append(it.next())
            except StopIteration:
                break
        return ans