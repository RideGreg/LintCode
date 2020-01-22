class Solution:
    """
    @param a: The array a
    @return: Return the minimum number of car
    """
    def getAnswer(self, a):
        a.sort()
        l, r = 0, len(a)-1
        ans = 0
        while l <= r:
            space = 4 - a[r]
            while l < r and space >= a[l]:
                space -= a[l]
                l += 1
            ans += 1
            r -= 1
        return ans

print(Solution().getAnswer([1,2,3,4])) #3
print(Solution().getAnswer([1,2,2,2])) #2
print(Solution().getAnswer([1,1,2,2])) #2
print(Solution().getAnswer([1,1,1,1])) #1
print(Solution().getAnswer([1,1,1,1,1])) #2