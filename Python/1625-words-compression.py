# There is a word compression method. For the string array s, first we assign the compression string to s[0],
# then splice the compression string with the s[1], the repeated part of the s[1]'s prefix and compression string's suffix will not be repeated,
# for example "aba" + "cba" --> "abacba", "aba" + "bac" --> "abac". Then splice the compression string with other strings in s
# in order to get the target compression string.

# Given the string array s, please output the first occurrence of each string in s in the target compression string.

class Solution:
    """
    @param s: the given strings
    @return: Output the first occurrence of each string in `s` in the target compression string.
    """
    def wordsCompression(self, s): # KMP
        def match(s, pattern):
            '''
            :param s: the compressed string
            :param pattern: the pattern to compress
            :rtype: tuple of (first matched position, maximum suffix matching length)
            '''
            # build nxt array
            nxt = [-1]
            pos = 0
            for char in pattern[1:]:
                nxt.append(nxt[pos] if char == pattern[pos] else pos)
                while pos >= 0 and char != pattern[pos]:
                    pos = nxt[pos]
                pos += 1
            nxt.append(pos)

            #
            fst_match = None
            pos = 0
            for sind, char in enumerate(s):
                if pos == len(pattern):
                    pos = nxt[pos]

                while pos >= 0 and char != pattern[pos]:
                    pos = nxt[pos]
                pos += 1

                if pos == len(pattern):
                    if fst_match is None:
                        fst_match = sind - len(pattern) + 1
                    # shouldn't put `pos = nxt[pos]` here
                    # otherwise will cause error with `match('abcd', 'cd', 'zz')`
            if fst_match is None:
                fst_match = len(s) - pos
            return fst_match, pos

        concat = ''
        ans = []
        for word in s:
            # first match, suffix match
            fst_match, match_len = match(concat, word)
            # update solution
            ans.append(fst_match)
            # concatenate the string
            concat = concat + word[match_len:]
        return ans

    # TLE: brute force
    def wordsCompression_bruteForce(self, s):
        concat = ''
        ans = []
        for word in s:
            for i in range(len(word), -1, -1):
                if concat.endswith(word[:i]):
                    concat = concat + word[i:]
                    ans.append(concat.index(word))
                    break
        return ans

print(Solution().wordsCompression(["aba","cba","acb","cb"])) # [0,3,2,3]
print(Solution().wordsCompression(["aaaba","abbb","aba","bbaa","baaa"])) # [0,4,2,11,12]