# Xiaohong went to the orchard to pick fruit. There are 2 baskets that can hold countless fruits,
# but each baskert can only hold one type of fruit. Start from the tree at any position and
# pick it to the right. Stop picking when one of the following two conditions occurs,
# 1. encountered the third type of fruit, no basket can be put,
# 2. meet the end. Returns the maximum number of fruits that can be picked.
# The fruit array is represented by arr.

class Solution:
    def pickFruits(self, arr):
        start, ans, fruitTypes = 0, 0, 0
        import collections
        counts = collections.defaultdict(int)
        for i, v in enumerate(arr):
            if counts[v] == 0:
                fruitTypes += 1
            counts[v] += 1

            while fruitTypes > 2:
                counts[arr[start]] -= 1
                if counts[arr[start]] == 0:
                    fruitTypes -= 1
                start += 1

            ans = max(ans, i - start + 1)
        return ans

print(Solution().pickFruits([1,2,1,3,4,3,5,1,2])) # 3
print(Solution().pickFruits([1, 2, 1, 2, 1, 2, 1])) # 7