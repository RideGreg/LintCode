# Given a secrect word, and an encoding rule as follows: Transform each letter in the secret,
# different letters can not be changed to the same letter. Such as banana -> xyzyzy,
# but banana can not become xyyyyy, because there is no way to decode back.

# Now input a very long string, and it is required to determine whether a substring exists in the string
# can be transformed by the above encoding rule. If exists, output string "yes", otherwise output "no".

# Idea: sliding window to check each possible substring with the same length with secret word !
# using dict to store matching relation between substring and secret word and set to store used char to make sure
# different char in substring have different matching char in secret word !
# two cases that violate our rule:
# 1) char in substring exists before accorindg to dict while dict[curr char in substring] != curr char in secret word;
# 2) char in secret word used before while corresponding char in substring does not exists in dict !
class Solution:
    """
    @param s: the long string
    @param word: the secrect word
    @return: whether a substring exists in the string can be transformed by the above encoding rule
    """
    def getAns(self, s, word):
        if len(s) < len(word): return "no"

        def check(t, s):
            s2t, usedt = {}, set()
            for i in range(len(s)):
                if s[i] in s2t:
                    if s2t[s[i]] != t[i]:
                        return False
                else:
                    if t[i] in usedt:
                        return False
                s2t[s[i]] = t[i]
                usedt.add(t[i])
            return True

        for i in range(len(s)-len(word)+1):
            if check(s[i:i+len(word)], word):
                return "yes"
        return "no"

print(Solution().getAns("abcabcd", "xyzxyz")) # yes
print(Solution().getAns("abca", "xyzd")) # yes
