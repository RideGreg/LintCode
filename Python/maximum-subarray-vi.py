# https://www.geeksforgeeks.org/find-the-maximum-subarray-xor-in-a-given-array/
# https://stackoverflow.com/questions/27470592/maximum-xor-among-all-subsets-of-an-array

class Solution:
    """
    @param nums: the array
    @return: the max xor sum of the subarray in a given array
    """
    def maxXorSubarray(self, array):
        if not array:  # special case the empty array to avoid an empty max
            return 0
        x = 0
        while True:
            y = max(array)
            if y == 0:
                return x
            # y has the leading 1 in the array
            x = max(x, x ^ y)
            # eliminate
            array = [min(z, z ^ y) for z in array]

print Solution().maxXorSubarray([1,2,3,4])
print Solution().maxXorSubarray([8,1,2,12,7,6])
print Solution().maxXorSubarray([4,6])
