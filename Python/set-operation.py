class Solution:
    """
    @param A: The set A
    @param B: The set B
    @return: Return the size of three sets
    """
    def getAnswer(self, A, B):
        A, B = set(A), set(B)
        return [len(A|B), len(A&B), len(A-B)]

print Solution().getAnswer([1,3,4,6], [1,5,10])