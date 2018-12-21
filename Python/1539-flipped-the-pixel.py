# An image is arranged in pixels of the two-dimensional array byte[][], where each element
# of the array represents a pixel bit (0 or 1). Now you need to flip these pixels,
# first flip the pixels of each row symmetrically, then flip the pixels on each bit (0->1,1->0).

class Solution:
    """
    @param Byte:
    @return: return the answer after flipped
    """
    def flippedByte(self, Byte):
        for i in range(len(Byte)):
            Byte[i] = [1-b for b in Byte[i][::-1]]
        return Byte

print(Solution().flippedByte([[1,0,1,1,0],[0,1,1,0,1],[1,1,0,1,0], [0,0,1,0,0]]))
# [[1,0,0,1,0],[0,1,0,0,1],[1,0,1,0,0],[1,1,0,1,1]]