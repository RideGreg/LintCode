'''
Time: O(n)
Space: O(n)

Given a string s of only 'A' and 'B', find the longest substring that satisfies 
the number of 'A' and 'B' are the same. Please output the length of this substring.

Example
Given s = "ABAAABBBA", return 8.
Given s = "AAAAAA", return 0.
'''

class Solution:
    """
    @param S: a String consists of a and b
    @return: the longest of the longest string that meets the condition
    """
    def getAns(self, S):
        prefixSum, ans = [0], 0
        for c in S:
            m = prefixSum[-1]-1 if c == 'A' else prefixSum[-1]+1
            prefixSum.append(m)

        ht = {}
        for i, p in enumerate(prefixSum):
            if p not in ht:
                ht[p] = i
            else:
                ans = max(ans, i-ht[p])
        return ans
