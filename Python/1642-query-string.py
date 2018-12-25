# Give a binary string str and an integer n to check if the substring of the string contains
# all binary representations of non-negative integers less than or equal to the given integer.

class Solution:
    def queryString(self, str, n):
        import math
        posMsb = int(math.log(n, 2))
        msb = 1 << posMsb
        cutoff = msb >> 1 if msb > 0 else -1
        return all(bin(i)[2:] in str for i in range(n, cutoff, -1)) and "yes" or "no"

print(Solution().queryString("0110", 3)) # yes
print(Solution().queryString("0110", 4)) # no

