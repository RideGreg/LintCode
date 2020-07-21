# 703
# Given an array nums of length n and an array req of length k , you need to fold the array as required, and output the result of the fold.
# 1.If req[i] = 0 means you should fold from left to right
# for example:
#
# 1 2 3 4 5 6 7 8  ==>   4 3 2 1
#                        5 6 7 8
# 2.If req[i] = 1 means you should fold from right to left
# for example:
#
# 1 2 3 4 5 6 7 8  ==>   8 7 6 5
#                        1 2 3 4
# More example:
#
# fold from left to right
# 4 3 2 1  ==>  6 5
# 5 6 7 8       3 4
#               2 1
#               7 8
#
#
# fold from right to left
# 6 5  ==>   8
# 3 4        1
# 2 1        4
# 7 8        5
#            6
#            3
#            2
#            7

class Solution:

    def folding(self, nums, req):

        f = len(nums)
        for d in req:
            f //= 2
            left, right = [], []
            for i, num in enumerate(nums):
                if (i // f) % 2 == 0:
                    left += num,
                else:
                    right += num,
            if d == 1:
                left, right = right, left
            nums = left[::-1] + right
        return nums

print(Solution().folding([1, 2, 3, 4, 5, 6, 7, 8], [0,0,1])) # [8, 1, 4, 5, 6, 3, 2, 7]
print(Solution().folding([1,2,3,4], [0,1])) # [4,1,2,3]
