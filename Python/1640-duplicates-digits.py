# Given an integer n, return the count of numbers that is less than
# or equal to n, and have duplicates digits.

# Refer to Leetcode 357 Count Numbers with Unique Digits

class Solution:
    """
    @param n: The integer n.
    @return: The count of numbers that <= n and have duplicates digits.
    """
    def countNumbers(self, n):
        s=str(n)
        bit=len(s)
        # count unique with length up to bit-1
        unique=self.countUniqueUpToLength(bit-1)
        # no need to consider number > 9999999999, because all digits are used,
        # no more unique digits
        if bit > 10:
            return n - unique

        # consider numbers with same length
        used=[] # used digits
        for i in range(bit-1):
            head = int(s[i])
            # mult is the count of usable digits (multiple) in current position
            if i==0:
                mult = head - 1 # digit 0 cannot used as beginning
            else:
                mult = head - sum(1 for x in used if x < head)

            if mult > 0:
                unique += mult * self.countUniqueInRemainBits(i, bit-i-1)

            if head not in used: # put head at current position, count remaining positions
                used.append(head)
            else: # not unique, no need to put head at current position and continue, i.e. 44xxx
                return n-unique

        start = 1 if bit == 1 else 0 # if single digit, 0 cannot be used as last digit
        unique += sum(1 for i in xrange(start, int(s[-1]) + 1) if i not in used)

        return n-unique

    # count of numbers with unique digits with length <= bit (not including number 0, as
    # when calculating count of numbers w/ repeated digits = n - #unique, n doesn't include 0 either)
    # The general dynamic programming formula: for k>=2, f(k) = 9*9*8*7 ... * 9-k+2.
    # bit <=:  0 1 2  3          4
    # #unique: 0 9 90 90+648=738 738+4536=5274
    def countUniqueUpToLength(self ,bit):
        if bit == 0: return 0

        count, fk = 9, 9
        for k in xrange(2, min(bit+1,11)):
            fk *= 10-(k-1)
            count += fk
        return count

    # bit is # of bits need to put digit at, i is positions already determined in original
    # input number, i.e. i+1 digits were used, only 10-(i+1) digits available, so start with 9-i
    def countUniqueInRemainBits(self,i,bit):
        if bit==0:
            return 1 # return value is used in multiplication
        ans, start = 1, 9-i
        for _ in range(bit):
            ans *= start
            start -= 1
        return ans

print(Solution().countNumbers(4567)) # 2060
print(Solution().countNumbers(3)) # 0
print(Solution().countNumbers(15)) # 1
print(Solution().countNumbers(21)) # 1
print(Solution().countNumbers(20)) # 1
print(Solution().countNumbers(100)) # 10
print(Solution().countNumbers(1000)) # 262
