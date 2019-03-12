# -*- encoding: utf-8 -*-

# Time: O(k), where k is the steps to 1 or a repeated number
# Space: O(k)

# Write an algorithm to determine if a number is happy.
#
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number
# by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay),
# or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Note: 证明非快乐数肯定会出现重复：任何一个4位或者4位以上的数字求各位平方和之后会比本身小， 三位数的各位平方和最大为81+ 81+81，
# 任何非欢乐数最后会在[1, 243]中间循环，所以肯定会出现重复，用set判断重复跳出无限循环

# 所有不快乐数的数位平方和计算，最後都会进入 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 的循环中。

class Solution:
    def isHappy(self, n):
        used = set()
        while n not in used and n != 1:
            used.add(n)
            n = sum(int(v) ** 2 for v in list(str(n)))
        return n == 1

    def isHappy2(self, n):
        used = set()
        while n not in used and n != 1:
            used.add(n)
            nextn = 0
            while n > 0:
                n, r = divmod(n, 10)
                nextn += r**2
            n = nextn
        return n == 1

print(Solution().isHappy(19)) # True, 19->82->68->100->1