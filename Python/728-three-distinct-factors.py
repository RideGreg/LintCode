# 728
# Given a positive integer n (1 <= n <= 10^18). Check whether a number has exactly
# three distinct factors, return true if it has exactly three distinct factors, otherwise false.

class Solution:
    """
    @param n: the given number
    @return:  return true if it has exactly three distinct factors, otherwise false
    """
    def isThreeDisctFactors(self, n):
        def isPrime(x):
            if x <= 1: return False
            if x <= 3: return True
            if x % 2 == 0 or x % 3 == 0:
                return False
            i = 5
            while i * i <= x:
                if x % i == 0 or x % (i+2) == 0:
                    return False
                i += 6
            return True

        sq = int(n ** 0.5)
        if sq * sq != n:
            return False
        return isPrime(sq)

    def isThreeDisctFactors_TLE(self, n):
        f = set()
        for i in range(1, int(n**0.5)+1):
            if n % i == 0:
                f.add(i)
                f.add(n//i)
                if len(f) > 3:
                    return False
        return len(f) == 3

print(Solution().isThreeDisctFactors(9)) # True
print(Solution().isThreeDisctFactors(10)) # False
print(Solution().isThreeDisctFactors(550220950190521)) # True

