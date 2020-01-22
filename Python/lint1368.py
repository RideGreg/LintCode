class Solution:
    """
    @param nums: the arrays
    @param k: the distance of the same number
    @return: the ans of this question
    """
    def sameNumber(self, nums, k):
        import collections
        d = collections.defaultdict(list)
        for i, n in enumerate(nums):
            if d[n] and i-d[n][0] < k:
                return 'YES'
            d[n] = [i]
        return 'NO'

print Solution().sameNumber([1,2,3,1,5,9,3], 4)
print Solution().sameNumber([1,2,3,5,7,1,5,1,3], 4)