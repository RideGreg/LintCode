class Solution:
    """
    @param k: The necessary distance of same kind of letters
    @param S: The original string
    @return: Return the number of '_' inserted before each position of the original string
    """
    def getAns(self, k, S):
        ans, n = [0], len(S)
        for i in xrange(n-1):
            for j in xrange(1, k):
                if i+j>=n: break
                if S[i+j] == S[i]:
                    ans.append(k-j)
                    break
                else:
                    ans.append(0)
        return ans

print(Solution().getAns(3, 'AABACCDCD'))
print(Solution().getAns(2, 'ABBA'))