# Given a word s, and a string set str. This word removes one letter at a time until there is only one letter
# in the word. Is there a sort of deletion in which all words are in str. For example, the word is 'abc',
#  the string set is {'a', 'ab', 'abc'}, if the order of deletion is 'c', 'b', and 'abc', 'ab', 'a' are
# all in the collection, so it is eligible.
# Output whether this combination meets the condition.

class Solution:
    def checkWord(self, s, str):
        strset = set(str)
        memo = set()

        def dfs(word):
            if not word: return True
            if word not in strset:
                return False

            for i in xrange(len(word)):
                nword = word[:i]+word[i+1:]
                if nword in memo:
                    continue

                if dfs(nword):
                    return True

                memo.add(nword)

            return False

        if s not in strset: return False
        return dfs(s)

print(Solution().checkWord("abcdbbdbadadacbcccabbcadddbca",
["abcdbbdbadadacbcccabbcadddbca","abcdbbdbadadacbcccabbcadddca","bdd","abbb","dbbcd","abcdbbdbadadacbcccabbca",
 "cbcacbd","accacaca","cbbcabcdd","abdacaadbb","bccaccbbdbb","acaadbccdaca","ddcdbddccccab","aaaddcdbcaabba",
 "ccabdddadcbbdaa","dddaccdbbbdcdbbd","aaddacccaacbccdac","bacaddaacacadbdbab","aaaacbbcabbdbbbdadd",
 "bbbabadccaacbdaaaaab","cbccaaddddcdcddccbaca","abcdbbdbadadacbcccab","bcadadaaddcbadcbdcabdcd",
 "acdcbcbdccbaacdcccdacbbb","cadbaabbaccbbccccccbcaacc","bddddbddbdcdbaaddccbacaccc","abcacbbaaddcdabcdbdaddbdbdb",
 "dbdabdcaaccdccdcbccadddacdda","abbdcaacdcacadbbbcbccaacdcdbb","aadddadcbda","abdbdbbadb","addccacaaabccdc",
 "abcdbbdbadadacbccb","dddcbdacccbaaacacccdbdd","cbabcacbccbddabaadbdbdcbaacd","cdcbcdddbcabbccbcbbbdabbadd",
 "a","cabbcacaadbaddcbaacc","cddbdba","abcdbbdbadadcb","abcdbbdbadadcbb","ad","aabadadcadcdcbdbbacdaabacaad",
 "abcd","abcdbd","abcdbbd","abcdbbdd","adddbcab","abcdbbdbad","abcdbbdbadd","abcdbbdbadad","abcdbbdbadadc",
 "ddabdbbacbcadbcacdacddaababc","cdcbddcabcbdacbbaddba","abcdbbdbadadacbcccabbcadca","abcdbbdbadadacbcccabbcaddca",
 "abcdbbdbadadacbcccabbcaca","abcdbbdbadadacbcccabbcca","aababdddbdc","dbdbcb","aaddaabcaadcd","daaaddbb",
 "bccdbdbadabcdbccbdcbacabc","bcadadcbb","babcdadadddabdaaadd","cccbadbbabaadaadcadccccdc","b","cdcbcabbbcaa",
 "cbaccaddddbbb","aabbcbbbaaccabdbabbcbddbdacb","abcdbbdbadadacbcccabba","abcdbbdbadadacbcccabb","badabd",
 "abccbccbbdbbcdbb","caadbcacbbcdabacca","ddacdcdbbcbb","cacbcabcdccda","abda","dcaaddaddadaddcdbbbbb","caddb",
 "bbcdbddbdcbcccabb","badb","cabcdccbadbbabbbdbbcdbad","ddcaddcdbacdcbadbbbbdbbcdc","b",
 "cccdcaabdcabcbbcaabababddda","dcadabcadadcbbcacdaccbb","abcdbbdbadadacbcccb","cbacbbacacbabdadc",
 "acbdacbaacaac","aacbccbbbbcacddaa","bcdbaab","caadcaadbaadababddcbbabaacbdd","badbbacbabcdabbcaddddc",
 "abcdbbdbadadcbcb","abcdbbdbadadcbccb","abd","abcdd","addcabbbdabaa","abcdbbdbd"]
)) # True
print(Solution().checkWord("abc", ["abc","ac","c"])) # True
print(Solution().checkWord("abc", ["abc","ab","c"])) # False