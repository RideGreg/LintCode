'''
1224. Count The Repetitions
Define S = [s,n] as the string S which consists of n connected strings s. For example, ["abc", 3] ="abcabcabc".

On the other hand, we define that string s1 can be obtained from string s2 if we can remove some characters from s2 such that it becomes s1.
For example, "abc" can be obtained from "abdbec" based on our definition, but it can not be obtained from "acbbe".

You are given two non-empty strings s1 and s2 (each at most 100 characters long) and two integers 0<=n1<=106 and 1<=n2<=106.
Now consider the strings S1 and S2, where S1=[s1,n1] and S2=[s2,n2]. Find the maximum integer M such that [S2,M] can be obtained from S1.

Example
Given:
s1="acb", n1=4
s2="ab", n2=2

Return: 2
'''
class Solution:
    """
    @param s1: the first string
    @param n1: the repeat times of the first string
    @param s2: the second string
    @param n2: the repeat times of the second string
    @return: the maximum integer
    """
    def getMaxRepetitions(self, s1, n1, s2, n2):
        if n1 == n2: n1 = n2 = 1

        # iterate all the big_s1
        cnt_s2 = [0]*(n1+1)
        nxtIdx_s2 = [0]*(n1+1)
        j, cnt = 0, 0

        for cur_s1 in range(1, n1+1):
            # for each iteration, find a s1 contains how many s2 (whole cnt + partial j).
            # next s1 comparison starts from s2[j].
            for i in range(len(s1)):
                if s1[i] == s2[j]:
                    j += 1
                    if j == len(s2): # match one s2
                        j = 0
                        cnt += 1
            cnt_s2[cur_s1], nxtIdx_s2[cur_s1] = cnt, j

            # check all repetition (less than cur_s1) of s1, whether contains same s2
            for prev_s1 in range(cur_s1):
                if nxtIdx_s2[prev_s1] == j: # found repeat pattern!!! no need to continue
                    prefixCount = cnt_s2[prev_s1]

                    repeats, mod_s1 = divmod(n1 - prev_s1, cur_s1 - prev_s1)
                    patternCount = (cnt_s2[cur_s1] - cnt_s2[prev_s1]) * repeats

                    postfixCount = cnt_s2[prev_s1 + mod_s1] - cnt_s2[prev_s1]

                    return (prefixCount + patternCount + postfixCount) // n2

        return cnt_s2[n1] // n2

    # TLE: brute force, repeatedly query long_s2 in long_s1
    def getMaxRepetitions_bruteforce(self, s1, n1, s2, n2):
        if n1 == n2:
            n1, n2 = 1, 1
        l1, l2 = len(s1), len(s2)
        i, j, ans = 0, 0, 0
        while i < l1*n1 and j < l2*n2:
            if s1[i%l1] == s2[j%l2]:
                j += 1
                if j == l2 * n2:
                    ans += 1
                    j = 0
            i += 1
        return ans


print(Solution().getMaxRepetitions('acb', 4, 'ab', 2)) #2
print(Solution().getMaxRepetitions('aaa', 3, 'aa', 1)) #4

print(Solution().getMaxRepetitions('acbaa', 5, 'aba', 1))
#5 prefixCount = 1, patternCount = 4, postfixCount = 0
# cnt_s2    [0, 1, 2, 0, 0]
# nxtIdx_s2 [0, 1, 1, 0, 0]
#      acba|a acba|a acbaa acbaa acbaa