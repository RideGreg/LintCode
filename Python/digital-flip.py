# -*- encoding: utf-8 -*-

"""
843. Digital Flip
Give you an array of 01. Find the minimum number of flipping steps so that the array meets the following rules:
The back of 1 can be either1 or 0, but0 must be followed by 0.

Example
Given array = [1,0,0,1,1,1], return 2.

Explanation:
Turn two 0s into 1s.
Given array = [1,0,1,0,1,0], return 2.

Explanation:
Turn the second 1 and the third 1 into 0.
Notice
The length of the given array n <= 100000.

Solution: Time: O(n) Space: O(1)
new0/new1: min steps needed to flip current index to 0 (or 1)
old0/old1: min steps needed to flip the last index to 0 (or 1)
0前面可以为1和0，而1前面只能为1.
"""

class Solution:
    """
    @param nums: the array
    @return: the minimum times to flip digit
    """
    def flipDigit(self, nums):
        old0, old1 = 0, 0
        for n in nums:
            new0 = min(old0, old1) + n # if n is 1, need flip one more time; n is 0, no flip needed
            new1 = old1 + (1 - n) # if n is 1, no flip needed; n is 0, need flip one more time
            old0, old1 = new0, new1
        return min(old0, old1)

    # TLE: O(n^2) recursion too many time if there is many 0 in the list
    # idea: return min from (either flip all 1s after the first 0, or flip the first 0 and recurse the flipped list)
    def flipDigit_recursion(self, nums):
        def recur(nums, n):
            firstZero = next(iter(i for i in xrange(n) if nums[i] == 0), n)
            if firstZero == n:
                return 0
            else:
                cur = sum(1 for x in nums[firstZero:] if x==1)
                nums[firstZero] = 1
                return min(cur, 1 + recur(nums, n))

        return recur(nums, len(nums))

print(Solution().flipDigit([1,0,0,1,1,1]))
print(Solution().flipDigit([1,0,1,0,1,0]))

