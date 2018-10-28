'''
Merge two given sorted integer array A and B into a new sorted integer array.

Example
A=[1,2,3,4]

B=[2,4,5,6]

return [1,2,2,3,4,4,5,6]

Challenge
How can you optimize your algorithm if one array is very large and the other is very small?
'''

class Solution:
    """
    @param A: sorted integer array A
    @param B: sorted integer array B
    @return: A new sorted integer array
    """
    def mergeSortedArray(self, A, B):
        # write your code here
        ret, i, j = [], 0, 0
        while i < len(A) and j < len(B):
            if A[i] <= B[j]:
                ret.append(A[i]) 
                i += 1
            else:
                ret.append(B[j])
                j += 1

        if i == len(A):
            ret.extend(B[j:])
        elif j == len(B):
            ret.extend(A[i:])

        return ret

    ''' For follow up challenge O(mlogn) where m<<<n
    def mergeSortedArray(self, A, B):
        # find the last insertion position
        from bisect import bisect_right

        small_arr = large_arr = None
        if len(A) < len(B):
            small_arr, large_arr = A, B
        else:
            small_arr, large_arr = B, A

        result, i = [], 0
        for num in small_arr:
            pos = bisect_right(large_arr, num)
            result += large_arr[i: pos]
            result.append(num)
            i = pos
        result += large_arr[i:]

        return result
    '''
