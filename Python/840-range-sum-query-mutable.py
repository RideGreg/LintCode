# Time: init: O(n), update: O(logn), query: O(logn)
# Space: O(n)

# Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.
# The update(i, val) function modifies nums by updating the element at index i to val.

# 1.The array is only modifiable by the update function.
# 2.You may assume the number of calls to update and sumRange function is distributed evenly.

class NumArray(object): # Bit Indexed Tree
    def __init__(self, nums):
        self.nums = [0] * len(nums)
        self.BITree = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.update(i, nums[i])

    def update(self, i, val):
        delta = val - self.nums[i]
        if delta == 0: return

        self.nums[i] = val
        i += 1
        while i <= len(self.nums):
            self.BITree[i] += delta
            i += i & (-i)

    def sumRange(self, i, j):
        def sum(i):
            s = 0
            i += 1
            while i > 0:
                s += self.BITree[i]
                i -= i & (-i)
            return s

        return sum(j) - sum(i-1)


class NumArray_segmentTree(object):
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * self.n + nums
        for i in reversed(range(1, self.n)):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, i, val):
        i += self.n
        if val != self.tree[i]:
            self.tree[i] = val
            while i > 0:
                sibling = i - 1 if i % 2 else i + 1
                self.tree[i / 2] = self.tree[i] + self.tree[sibling]
                i /= 2

    def sumRange(self, i, j):
        i, j, s = i + self.n, j + self.n, 0
        while i <= j:
            if i % 2:
                s += self.tree[i]
                i += 1
            if j % 2 == 0:
                s += self.tree[j]
                j -= 1
            i /= 2
            j /= 2
        return s

obj = NumArray([0,9,5,7,3])
print(obj.sumRange(4, 4)) # 3
print(obj.sumRange(2, 4)) # 15
print(obj.sumRange(3, 3)) # 7
obj.update(4, 5)
obj.update(1, 7)
obj.update(0, 8)
print(obj.sumRange(1, 2)) # 12
obj.update(1, 9)
print(obj.sumRange(4, 4)) # 5
obj.update(3, 4)