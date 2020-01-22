class Solution:
    """
    @param k: The k
    @param a: The A
    @param b: The B
    @return: The answer
    """
    def addition(self, k, a, b):
        a, b = a.lstrip('0'), b.lstrip('0')
        l = max(len(a), len(b))
        ans, c = '', 0
        for i in xrange(1, l+1):
            ai = a[-i] if len(a)>=i else 0
            bi = b[-i] if len(b)>=i else 0
            sum = int(ai) + int(bi) + c
            c = 1 if sum >=k else 0
            ans = str(sum%k) + ans
        return ans if c == 0 else '1'+ans

print Solution().addition(2, '11', '1')
print Solution().addition(3, '12', '1')
print Solution().addition(3, '12', '001')