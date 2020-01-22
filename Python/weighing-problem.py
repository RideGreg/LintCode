class Solution:
    """
    @param n: The number of coins
    @return: The Minimum weighing times int worst case
    """
    def minimumtimes(self, n):
        import math
        ans = 1
        while n > 3:
            n = math.ceil(n/3)
            ans += 1
        return ans
