# Time: min(MlogM, NlogM), where M, N is the length of input array a and b
# Space: O(N)

# Given two integer arrays a and b,please find the number in a with the minimal distance
# between each value in b (the distance between two numbers means the absolute value of two numbers),
# if there are several numbers in a have same distance between b[i], output the smallest number.
# The output should be an array of length b.length to represent the answer.

class Solution:
    """
    @param a: array a
    @param b: the query array
    @return: Output an array of length `b.length` to represent the answer
    """
    def minimalDistance(self, a, b):
        def search(a, n): # search for 2 closest indices, then compare these 2 only
            l, r = 0, len(a)-1
            while l < r - 1:
                m = l + (r-l)//2
                if a[m] == n:
                    return n
                elif a[m] < n:
                    l = m    # values before index m are much less, discard; but keep m
                else:
                    r = m    # values after index m are much larger, discard; but keep m
            return a[l] if abs(a[l]-n) <= abs(a[r]-n) else a[r]

            ''' # compare each m
            delta, ans = float('inf'), float('inf')
            while l <= r:
                m = l + (r-l)//2
                if a[m] == n:
                    return n
                else:
                    if abs(a[m]-n) < delta or (abs(a[m]-n)==delta and a[m]<ans):
                        delta, ans = abs(a[m]-n), a[m]
                    if a[m] < n:
                        l = m + 1
                    else:
                        r = m - 1
            '''
            return ans

        a.sort()
        ans = []
        for j in b:
            ans.append(search(a, j))
        return ans

print(Solution().minimalDistance([5,1,2,3], [2,4,2])) # [2,3,2]
print(Solution().minimalDistance([5,3,1,-1,6], [4,8,1,1])) # [3,6,1,1]