# Narcissistic Number is a number that is the sum of its own digits each raised to the power of the number of digits.
#
# For example the 3-digit decimal number 153 is a narcissistic number because 153 = 13 + 53 + 33.
# And the 4-digit decimal number 1634 is a narcissistic number because 1634 = 14 + 64 + 34 + 44.
#
# Given n, return all narcissistic numbers with n digits.

# Brute Force
class Solution:
    """
    @param n: The number of digits
    @return: All narcissistic numbers with n digits
    """
    def getNarcissisticNumbers(self, n):
        res = []
        for x in range([0, 10**(n-1)][n > 1], 10**n):
            y, s = x, 0
            while x > 0:
                x, r = divmod(x, 10)
                s += r**n
            if s == y:
                res.append(y)
        return res

print(Solution().getNarcissisticNumbers(3)) # [153, 370, 371, 407]