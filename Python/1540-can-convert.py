# Time:  O(min(s, t))
# Space: O(1)

# Given two string S and T, determine if S can be changed to T by deleting some letters (including 0 letter)

class Solution:
    """
    @param s: string S
    @param t: string T
    @return: whether S can convert to T
    """
    def canConvert(self, s, t):
        if s is None or t is None: return False

        j = 0
        for i in xrange(len(s)):
            if s[i] == t[j]:
                j += 1
                if j == len(t):
                    return True
        return j == len(t)

print(Solution().canConvert("lintcode", "lint")) # True