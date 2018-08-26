'''
Time:  O(n)
Space: O(n)

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

Example
Given pattern = "abba", str = "dog cat cat dog", return true.
Given pattern = "abba", str = "dog cat cat fish", return false.
Given pattern = "aaaa", str = "dog cat cat dog", return false.
Given pattern = "abba", str = "dog dog dog dog", return false.
'''

class Solution:
    """
    @param pattern: a string, denote pattern string
    @param str: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """
    def wordPattern(self, pattern, str):
        words = str.split()
        if len(pattern) != len(words): return False
        
        p2w, w2p = {}, {}
        from itertools import izip
        for a, b in izip(pattern, words):
            amap, bmap = p2w.get(a), w2p.get(b)
            if amap is None and bmap is None:
                p2w[a], w2p[b] = b, a
            elif amap != b:
                return False
        return True
