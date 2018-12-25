# -*- encoding=utf-8 -*-

# Given an array with n integers. Splitting it into subsequences of strictly descending order.
# Output the minimum number of subsequences you can get by splitting.

class Solution:
    # O(nlogn): DP + Binary Search
    # suppose have existing set of sequences, the next element should try to fit with one of them, otherwise start a new sequence

    # 用一个list保存每一个subsequence的tail。如果新的元素可加入现有数列，就用binary search找到比这个新元素大的所有tail中最小的那个，替换掉
    # 如果找不到比新元素小的tail，这个新元素会开始一个单独的subsequence,就把这个新元素append在list后面。最后list的长度就是subsequence的个数
    # 数组的遍历是n，每次在list查找由于用的二分是logn ，总体复杂度是O(nlogn)

    # 其实是耐心排序 patience sorting：
    # http://www.cs.princeton.edu/courses/archive/spring13/cos423/lectures/LongestIncreasingSubsequence-2x2.pdf
    # Theorem: "Min number of piles = max length of an IS"(对于这道题来说IS是 >=)

    # 这个排序的关键在建桶和入桶规则上
    # 建桶规则:如果没有桶,新建一个桶;如果不符合入桶规则那么新建一个桶
    # 入桶规则:只要比桶里最上边的数字小即可入桶,如果有多个桶可入,那么按照从左到右的顺序入桶即可
    # similar: Stacking Boxes (ask what's the minimum number of stacks for all the boxes)

    def LeastSubsequences(self, arrayIn):
        import bisect
        seqEnd = []
        for a in arrayIn:
            pos = bisect.bisect_right(seqEnd, a)
            if pos == len(seqEnd):
                seqEnd.append(a)
            else:
                seqEnd[pos] = a
        return len(seqEnd)

    # O(n^2)
    def LeastSubsequences_DP(self, arrayIn):
        n = len(arrayIn)
        dp, ans = [1] * n, 1
        for j in range(1, n):
            for i in range(j):
                if arrayIn[i] <= arrayIn[j]:
                    dp[j] = max(dp[j], dp[i]+1)
            ans = max(ans, dp[j])
        return ans

print(Solution().LeastSubsequences([5,2,4,3,1,6])) # 3
print(Solution().LeastSubsequences([1,1,1])) # 3