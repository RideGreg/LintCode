# Given a pattern and a string str, find if str follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

class Solution:
    def wordPattern(self, pattern, teststr):
        strs = teststr.split()
        if len(pattern) != len(strs):
            return False

        p2s, usedword = {}, set()
        import itertools
        for c, word in itertools.izip(pattern, strs):
            if c in p2s:
                if word != p2s[c]:
                    return False
                continue

            if word in usedword:
                return False
            p2s[c] = word
            usedword.add(word)
        return True

print(Solution().wordPattern("abba", "dog cat cat dog")) # True
print(Solution().wordPattern("abba", "dog cat cat fish")) # False
print(Solution().wordPattern("aaaa", "dog cat cat dog")) # False
print(Solution().wordPattern("abba", "dog dog dog dog")) # False