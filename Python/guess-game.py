class Solution:
    """
    @param a: The array a
    @return: Return the minimum cost
    """
    def getAnswer(self, a):
        if len(a) <= 1:
            return 0
        elif len(a) == 2:
            return min(a)
        elif len(a) == 3:
            return min(a[1], a[0]+a[2])
        else:
            ans = float('inf')
            for i in xrange(1, len(a)-2):
                cur = a[i] + max(self.getAnswer(a[:i]), self.getAnswer(a[i+1:]))
                ans = min(ans, cur)
            return ans

print(Solution().getAnswer([33,41,17,51,61,98,96,60,65,43])) #174 = 17+61+96
print(Solution().getAnswer([1, 100, 1])) #2
print(Solution().getAnswer([1,3,5,1,1,8,4])) #5 =
print(Solution().getAnswer([69,89,11,34,49])) #80
print(Solution().getAnswer([74,71,44,97,36,8,60,59,35,20,34,70,57,57,28,80,41,4,88,71])) #131
