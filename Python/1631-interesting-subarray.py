# If there are no more than two values in a subarray, the subarray is interesting.
# Given an array a, find the longest interesting subarray. Output the maximum length.

class Solution:
    # 1. calculate ans in each iteration to avoid forgetting the last valid sub-array
    # 2. let start pointer go forward to guarantee O(n)
    def maxLen(self, a):
        k = 2
        start, ans, uniqueValue = 0, 0, 0
        import collections
        counts = collections.defaultdict(int)
        for i, v in enumerate(a):
            if counts[v] == 0:
                uniqueValue += 1
            counts[v] += 1

            # check if start pointer needs go forward
            while uniqueValue > k:
                counts[a[start]] -= 1
                if counts[a[start]] == 0:
                    uniqueValue -= 1
                start += 1

            ans = max(ans, i-start+1)
        return ans


    def maxLen_lastPos(self, a): # try to find the min lastPos makes Time O(n*k), not linear
        k = 2
        lastPos, start, ans = {}, 0, 0
        for i, v in enumerate(a):
            # when values are more than allowed, evict one
            if v not in lastPos and len(lastPos) >= k:
                ans = max(ans, i-start)
                removeKey = min(lastPos, key=lastPos.get)
                start = lastPos[removeKey] + 1
                del lastPos[removeKey]

            lastPos[v] = i
        return max(ans, i+1-start)

print(Solution().maxLen([1,2,1,3])) #3
print(Solution().maxLen([1,1,1,1])) #4
