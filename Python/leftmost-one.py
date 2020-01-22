class Solution:
    """
    @param arr: The 2-dimension array
    @return: Return the column the leftmost one is located
    """
    def getColumn(self, arr):
        if not arr:
            return -1

        for j in xrange(len(arr[0])):
            if any(arr[i][j] for i in xrange(len(arr))):
                return j
        return -1

print Solution().getColumn([[0,0,0,1],[1,1,1,1]])
print Solution().getColumn([[0,0,0,1],[0,1,1,1]])