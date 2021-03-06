'''
Given two sorted integer arrays A and B, merge B into A as one sorted array.

Example
A = [1, 2, 3, empty, empty], B = [4, 5]

After merge, A will be filled as [1, 2, 3, 4, 5]

Notice
You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B.
The number of elements initialized in A and B are m and n respectively.
'''

class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        # write your code here
        i = m + n
        while m >= 1 and n >= 1:
            if A[m-1] < B[n-1]:
                A[i-1] = B[n-1]
                n -= 1
            else:
                A[i-1] = A[m-1]
                m -= 1
            i -= 1
        
        if n >= 1:
            A[:n] = B[:n]
