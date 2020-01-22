'''
1585. Moving Stones
There are n stones distributed on the x-axis, and their positions are represented by an array of arr. It is now required to move these stones to 1, 3, 5, 7, 2n-1 or 2, 4, 6, 8, 2n. That is to say, these stones are required to move to odd-numbered bits starting from 1 or consecutive even-numbered bits starting from 2. Returns the minimum number of moves. You can only move 1 stone at a time, only move the stone one unit to the left or one unit to the right. You cannot have two stones at the same time in the same location.

Example
Give arr=[5,4,1] and return 1.

Explanation：
You only need to move the stone in position 4 to the left to 3,
[1,3,5], in line with the requirements.
Give arr=[1,6,7,8,9] and return 5.

Explanation：
The optimal mobility scheme is to move 1 to 2, move 6 to 4, move 7 to 6, and move 9 to 10.
The cost is 1+2+1+1=5.
Notice
1 \leq n \leq 100001≤n≤10000
1 \leq arr[i] \leq 1000001≤arr[i]≤100000
'''
class Solution:
    """
    @param arr: the positions
    @return: minimum number of moves
    """
    def movingStones(self, arr):
        arr.sort()
        n = len(arr)
        d1, d2 = range(1,2 *n,2), range(2, 2 * n +1,2)

        def foo(s1, s2):
            a, b = sorted(list(s1 -s2)), sorted(list(s2 -s1))
            return sum(abs( m -n) for m ,n in zip(a ,b))

        return min(foo(set(d1), set(arr)), foo(set(d2), set(arr)))

print(Solution().movingStones([5,4,1]))
print(Solution().movingStones([1,6,7,8,9]))