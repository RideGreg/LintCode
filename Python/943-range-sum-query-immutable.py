# Time: O(1)
# Space: O(n)

# Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.
# You may assume that the array does not change.
# There are many calls to sumRange function.

class NumArray(object):

    def __init__(self, nums):
        self.sums = [0]
        for n in nums:
            self.sums.append(self.sums[-1] + n)

    def sumRange(self, i, j):
        return self.sums[j + 1] - self.sums[i]

obj = NumArray([-2, 0, 3, -5, 2, -1])
print(NumArray.sumRange(0,2)) # 1
print(NumArray.sumRange(2,5)) # -1
print(NumArray.sumRange(0,5)) # -3
