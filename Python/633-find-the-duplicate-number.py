# -*- encoding: utf-8 -*-

# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
#
# Example
# Given nums = [5,5,4,3,2,1] return 5
# Given nums = [5,4,4,3,2,1] return 4
#
# Notice
# You must not modify the array (assume the array is read only). (sort in-place)
# You must use only constant, O(1) extra space. (sort externally; counter)
# Your runtime complexity should be less than O(n^2). (2 loops)
# There is only one duplicate number in the array, but it could be repeated more than once.


class Solution:
    def findDuplicate(self, nums):  # Time O(n)
    # 1 快慢指针的方法 Time O(n)
    # 要做这个题你首先需要去做一下 Linked List Cycle 这个题。
    # 如果把数据看做一个 LinkedList，第i个位置上的值代表第i个点的下一个点是什么的话，我们就能画出一个从0出发的，一共有 n+1 个点的LinkedList。
    # 可以证明的一件事情是，这个 Linked List 一定存在环。因为无环的 Linked List 里 非空next 的数目和节点的数目关系是差一个（节点多，非空next少）
    #
    # 那么，我们证明了这是一个带环链表。而我们要找的重复的数，也就是两个点都指向了同一个点作为 next 的那个点。也就是环的入口。
    #
    # 因此完全套用 Linked List Cycle 这个题快慢指针的方法即可。
    #
    # 什么是快慢指针算法？
    # 从起点出发，慢指针走一步，快指针走两步。因为有环，所以一定会相遇。
    # 相遇之后，把其中一根指针拉回起点，重新走，这回快慢指针都各走一步。他们仍然会再次相遇，且相遇点为环的入口。
        if len(nums) <= 1: return -1
        s, f = nums[0], nums[nums[0]]
        while s != f:
            s, f = nums[s], nums[nums[f]]  # found the meet position

        f = 0
        while f != s:
            f = nums[f]
            s = nums[s]
        return s

    def findDuplicate_binarySearch(self, nums): # Time O(nlogn)
    # binary search: 答案的範圍會在start, end = 1, max(nums)之間，去計算小於等於mid的個數
    # 然後來縮小範圍.
    # 或者这样解释：九章算法强化班中讲过的基于值的二分法。
    #     这个题比较好的理解方法是画一个坐标轴：
    #
    #     x轴是0, 1, 2, ...n。
    #     y轴是对应的 <= x的数的个数，比如 <= 0的数的个数是0，就在（0, 0）这个坐标画一个点。 <= n
    #     的数的个数是n + 1个，就在(n, n + 1)画一个点。

    # 我们可以知道这个折线图的有如下的一些属性：
    #
    # 大部分时候，我们会沿着斜率为 1 的那条虚线前进
    # 如果出现了一些空缺的数，就会有横向的折线
    # 一旦出现了重复的数，就会出现一段斜率超过 1 的折线
    # 斜率超过 1 的折线只会出现一次
    # 试想一下，对比 y=x 这条虚线，当折线冒过了这条虚线出现在这条虚线的上方的时候，一定是遇到了一个重复的数。
    # 一旦越过了这条虚线以后，就再也不会掉到虚线的下方或者和虚线重叠。
    # 因为折线最终会停在 (n,n+1) 这个位置，如果要从 y=x 这条虚线或者这条虚线的下方到达 (n,n+1) 这个位置，
    # 一定需要一个斜率 > 1的折线段，而这个与题目所说的重复的数只有一个就是矛盾的。因此可以证明，斜率超过1 的折线只会出现1次，
    # 且会将折线整体带上 y=x 这条虚线的上方。因此第一个在 y=x 上方的 x 点，就是我们要找的重复的数。
    #
    # 时间复杂度是 O(nlogn)
        l, r = 1, len(nums)-1
        while l < r:
            m = l + (r-l)/2
            if sum(1 for n in nums if n <= m) <= m: # m not ok
                l = m + 1
            else: # m may be the answer; value larger than m can be discarded
                r = m

        return l

print(Solution().findDuplicate([1,1])) # 1
print(Solution().findDuplicate([5,5,4,3,2,1])) # 5
print(Solution().findDuplicate([5,4,4,3,2,1])) # 4
