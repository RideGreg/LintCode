# Time O(nlogn)
# Space O(1)

# There are n different tasks, the execution time of tasks are t[], and the
# probability of success are p[]. When a task is completed or all tasks fail,
# the operation ends. Tasks can be performed in a different order, and it is
# expected that in different order the time to stop the action is generally different.
#
# Please answer in what order to perform the task (task index is 1-based)
# in order to make the duration of the action the shortest time? If the expected
# end time of the two task sequences is the same, the lexicographic minimum
# order of tasks is returned.

# 1 <= n <= 50, 1 <= ti <= 10, 0 <= pi <= 1

# Example 1: Given n=1, t=[1], p=[1.0], return [1].
# Explanation:The shortest expected action end time is 1.0*1+(1.0-1.0)*1=1.0

# Example 2:
# Given n=2, t=[1,2], p=[0.3, 0.7], return [2,1].
# Explanation:
# The expected action end time for [2, 1] is
# 0.7 * 2      + (1.0-0.7)*0.3*(2+1) + (1.0-0.7)*(1.0-0.3)*(2+1)=2.3
# task 2 success   task 2 fail + 1 succ   task 2 and 1 fail
# p2 * t2 + (1-p2) * (t1 + t2) = (t1+t2) - p2t1 = (t1+t2)/p1p2 - t1/p1

# The expected action end time for [1, 2] is
# 0.3 * 1      + (1.0-0.3)*0.7*(1+2) + (1.0-0.3)*(1.0-0.7)*(1+2)=2.4
# task 1 success   task 1 fail + 2 succ   task 1 and 2 fail
# p1 * t1 + (1-p1) * (t1 + t2) = (t1+t2) - p1t2 = (t1+t2)/p1p2 - t2/p2

# solution: 拿 time/probability = ratio, ratio 小的排在前面
# 题目要求是求出一个期望时间最短。ratio越小，说明这个任务完成的概率越高或者时间越少，
# 这就是我们想要找的那一个最具有效率的task。

class Solution(object):
    def getOrder(self, n, t, p):
        return sorted(list(range(1, n+1)), key=lambda x: t[x-1]/p[x-1])

print(Solution().getOrder(1, [1], [1.0])) # [1]
print(Solution().getOrder(2, [1, 2], [0.3, 0.7])) # [2, 1]
print(Solution().getOrder(2, [1, 2], [0.3, 0.6])) # [1, 2] same ratio
