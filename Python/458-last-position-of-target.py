# Find the last position of a target number in a sorted array. Return -1 if target does not exist.

class Solution:
    def lastPosition(self, nums, target):
        import bisect
        i = bisect.bisect_right(nums, target)
        return i-1 if i > 0 and nums[i-1] == target else -1
        '''
        l, r = 0, len(nums)
        while l < r:
            m = l + (r-l)//2
            if nums[m] <= target:
                l = m + 1
            else:
                r = m
        return l-1 if l > 0 and nums[l-1] == target else -1
        '''

print(Solution().lastPosition([1, 2, 2, 4, 5, 5], 2)) # 2
print(Solution().lastPosition([1, 2, 2, 4, 5, 5], 5)) # 5
print(Solution().lastPosition([1, 2, 2, 4, 5, 5], 6)) # -1