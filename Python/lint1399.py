class Solution:
    """
    @param list: The coins
    @param k: The k
    @return: The answer
    """
    def takeCoins(self, list, k):
        ans = float('-inf')
        prefix = [0]
        for i in xrange(len(list)):
            prefix.append(prefix[-1]+list[i])
        for j in xrange(k+1):
            ans = max(ans, prefix[j]+(prefix[-1]-prefix[-1-(k-j)]))
        return ans

print Solution().takeCoins([5,4,3,2,1,6],3)