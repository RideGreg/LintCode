# Time:  O(N∗(M+N)), where M, N are the lengths of strings A, B. We create two strings A * r, A * (r+1)
# which have length at most O(M+N). This check of if B is a substring of A takes naively the product of their lengths.
# Space: O(M+N)

# Given two strings A and B, find the minimum number of times A has to be repeated such that B is a substring of it.
# If no such solution, return -1.

# Rolling hash solution has time O(M+N) see Leetcode

class Solution:
    """
    @param A: a string
    @param B: a string
    @return: return an integer
    """
    def repeatedStringMatch(self, A, B):
        # intuition: at least longer than B, at most B's length + repeat one more time
        # code is from cc189@lintcode https://www.linkedin.com/in/cc189/ https://cc189.github.io/

        r = -(-len(B)//len(A)) # same as int(math.ceil( float(len(B)) / len(A) ))
        for i in [0,1]:
            if B in A*(r+i):
                return r + i
        return -1

    def repeatedStringMatch2(self, A, B):
        for start in xrange(len(B)): # too many comparison
            if B[:start+1] not in A:
                break
        else: # for loop completes normally
            return 1

        ans = 1
        while start < len(B):
            if not A.startswith(B[start:start+len(A)]):
                return -1
            ans += 1
            start += len(A)
        return ans

import timeit
s1 = 'a'*1000
s2 = 'a'*900 + 'b'
print(timeit.timeit('Solution().repeatedStringMatch(s1, s2)', 'from __main__ import Solution, s1, s2', number=2000)) # 0.02 sec
print(timeit.timeit('Solution().repeatedStringMatch2(s1, s2)', 'from __main__ import Solution, s1, s2', number=2000)) #1.88 sec

print(Solution().repeatedStringMatch('a', 'a')) # 1
print(Solution().repeatedStringMatch('aa', 'a')) # 1
print(Solution().repeatedStringMatch('a', 'aa')) # 2
print(Solution().repeatedStringMatch('abcd', 'cdabcdab')) # 3
print(Solution().repeatedStringMatch('abcd', 'cdabcdabcd')) # 3
print(Solution().repeatedStringMatch('abcd', 'cdabcdabcda')) # 4
print(Solution().repeatedStringMatch('abcd', 'cdabcdabcdd')) # -1
