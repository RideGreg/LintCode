# Time O(n)
# Space O(1)

# Given an integer array, find a continuous subarray where the sum of numbers
# is the biggest. Your code should return the index of the first number
# and the index of the last number. (If their are duplicate answer,
# return the minimum one in lexicographical order)


class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySum(self, A):
        msum, ans = float('-inf'), []
        cur, left, right = 0, 0, 0
        for i, a in enumerate(A):
            if cur >= 0:
                cur, right = cur + a, i
            else:
                cur, left, right = a, i, i

            if cur > msum:
                msum, ans = cur, [left, right]
        return ans

print(Solution().continuousSubarraySum([-3, 1, 3, -3, 4])) # [1, 4]
print(Solution().continuousSubarraySum([0, 1, 0, 1])) # [0, 3]