'''
一般的数据库进行horizontal shard的方法是指，把id对数据库服务器总数n取模，然后来得到他在哪台机器上。这种方法的缺点是，当数据继续增加，
我们需要增加数据库服务器，将n变为n+1时，几乎所有的数据都要移动，这就造成了不consistent。为了减少这种naive的hash方法(%n)带来的缺陷，
出现了一种新的hash算法：一致性哈希的算法——Consistent Hashing。这种算法有很多种实现方式，这里我们来实现一种简单的 Consistent Hashing。

将id对360取模，假如一开始有3台机器，那么让3台机器分别负责0~119, 120~239, 240~359的三个部分。那么模出来是多少，查一下在哪个区间，就去哪台机器。
当机器从 n 台变为 n+1 台了以后，我们从n个区间中，找到最大的一个区间，然后一分为二，把一半给第n+1台机器。
比如从3台变4台的时候，我们找到了第3个区间0~119是当前最大的一个区间，那么我们把0~119分为0~59和60~119两个部分。0~59仍然给第1台机器，60~119给第4台机器。
然后接着从4台变5台，我们找到最大的区间是第3个区间120~239，一分为二之后，变为 120~179, 180~239。
假设一开始所有的数据都在一台机器上，请问加到第 n 台机器的时候，区间的分布情况和对应的机器编号分别是多少？

If the maximal interval is [x, y], and it belongs to machine id z, when you add a new machine with id n, you should divide [x, y, z] into two intervals:
[x, (x + y) / 2, z] and [(x + y) / 2 + 1, y, n]

E.g. for n=5, [
  [0,44,1],
  [45,89,5],
  [90,179,3],
  [180,269,2],
  [270,359,4]
]
'''

# Time: O(nlogn) if heap, O(n^2) if not using heap
# Space: O(n) if heap, O(1) if not using heap

class Solution:
    """
    @param: n: a positive integer
    @return: n x 3 matrix
    """

    # minHeap comparison order is maxRange->minServerId, comparison key is -range*1000+serverId, record is index in ans list. USE THIS: BEST performance
    def consistentHashing_heap_serverorder(self, n): #USE THIS
        import heapq
        ans, h = [[0, 359, 1]], []
        heapq.heappush(h, (-360*1000+1, 0))

        for i in xrange(2, n + 1):
            index = heapq.heappop(h)[1]
            s, e, maxId = ans[index]

            ans[index][1] = (s+e)/2   # new 'end'
            range = (s+e)/2 - s + 1
            heapq.heappush(h, (-range*1000+maxId, index))

            ans.append([(s+e)/2+1, e, i])
            range = e - (s+e)/2
            heapq.heappush(h, (-range*1000+i, len(ans)-1))
        return ans

    # minHeap comparison key is (maxRange, minServerId), value is obj as index keeps changing. Second faster
    def consistentHashing_heap_bucketorder(self, n):
        import heapq
        ans, h = [[0, 359, 1]], []
        heapq.heappush(h, (-360*1000+1, [0, 359, 1]))

        for i in xrange(2, n + 1):
            obj = heapq.heappop(h)[1]
            index, (s, e, maxId) = ans.index(obj), obj   # obj is usually at front of ans, so much faster than O(n)

            ans[index][1] = (s+e)/2
            range = (s+e)/2 - s + 1
            heapq.heappush(h, (-range*1000+maxId, ans[index]))

            ans.insert(index+1, [(s+e)/2+1, e, i])
            range = e - (s+e)/2
            heapq.heappush(h, (-range*1000+i, ans[index+1]))
        return ans


    def consistentHashing_jiuzhang_linearscan(self, n): # ans ordered by server id 1-n
        results = [[0, 359, 1]]
        for i in xrange(1, n):
            index = 0
            for j in xrange(i):
                if results[j][1] - results[j][0] > results[index][1] - results[index][0]:
                    index = j

            x, y = results[index][0], results[index][1]
            results[index][1] = (x + y) / 2
            results.append([(x + y) / 2 + 1, y, i + 1])
        return results

    # naive: new bucket is inserted after the divided bucket, so next bucket to be divided is the one after new bucket.
    # Wrong becuase the next bucket picked in this way is not necessarily biggest, e.g. for groups 23/22/23/22.
    def consistentHashing_wrong(self, n):
        ans = [[0, 359, 1]]
        cur = 0
        for i in xrange(2, n + 1):
            s, e, oldId = ans[cur]
            ans[cur] = [s, (s+e)/2, oldId]
            ans.insert(cur+1, [(s+e)/2+1, e, i])
            cur = (cur + 2) % len(ans)
        return ans


import timeit
#[[0, 44, 1], [45, 89, 5], [90, 134, 3], [135, 179, 7], [180, 224, 2], [225, 269, 6], [270, 314, 4], [315, 359, 8]]
a = Solution().consistentHashing_heap_bucketorder(8)
#[[0, 44, 1], [180, 224, 2], [90, 134, 3], [270, 314, 4], [45, 89, 5], [225, 269, 6], [135, 179, 7], [315, 359, 8]]
b = Solution().consistentHashing_heap_serverorder(8)
c = Solution().consistentHashing_jiuzhang_linearscan(8)
print a, "\n", b, "\n", c
print b == c # equal
print a == c # not equal
print timeit.timeit('Solution().consistentHashing_heap_bucketorder(18)', 'from __main__ import Solution', number=1000)
print timeit.timeit('Solution().consistentHashing_heap_serverorder(18)', 'from __main__ import Solution', number=1000)
print timeit.timeit('Solution().consistentHashing_jiuzhang_linearscan(18)', 'from __main__ import Solution', number=1000)
#0.0637052059174
#0.052943944931 BEST
#0.11460185051

print timeit.timeit('Solution().consistentHashing_heap_bucketorder(360)', 'from __main__ import Solution', number=50)
print timeit.timeit('Solution().consistentHashing_heap_serverorder(360)', 'from __main__ import Solution', number=50)
print timeit.timeit('Solution().consistentHashing_jiuzhang_linearscan(360)', 'from __main__ import Solution', number=50)
#0.111467123032
#0.058678150177 BEST
#1.84765601158