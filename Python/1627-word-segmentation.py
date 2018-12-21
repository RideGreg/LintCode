# Given a long string S, only include normal English words, words are separated by a single space,
# and give you a positive integer. Please divide the string into several lines and the number of lines is minimum.
# Requirement 1: You can only wrap between words. The same word cannot be separated;
# Requirement 2: Each line cannot be more than k character after the division.

class Solution:
    def wordSegmentation(self, s, k):
        words = s.split()
        ans = []
        leng, line = len(words[0]), words[0]
        for w in words[1:]:
            if leng + 1 + len(w) <= k:
                leng += 1+len(w)
                line = line + ' ' + w
            else:
                ans.append(line)
                leng, line = len(w), w
        return ans + [line]

print(Solution().wordSegmentation("aaaa bbb cccc ddd ee ff ggggg", 8))
# ["aaaa bbb","cccc ddd","ee ff","ggggg"]
