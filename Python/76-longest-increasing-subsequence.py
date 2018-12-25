# Time: O(nlogn)
# Space: O(n)

# Given a sequence of integers, find the longest increasing subsequence (LIS).
# You code should return the length of the LIS.

# Solution: Dynamic Programming + Binary Search
class Solution:
    def longestIncreasingSubsequence(self, nums):
        import bisect
        LISend = []
        for n in nums:
            pos = bisect.bisect_left(LISend, n)
            if pos == len(LISend):
                LISend.append(n)
            else:
                LISend[pos] = n
        return len(LISend)
