# Given a string and an offset, rotate string by offset. (rotate from left to right)
#
# Example
# Given "abcdefg".
#
# offset=0 => "abcdefg"
# offset=1 => "gabcdef"
# offset=2 => "fgabcde"
# offset=3 => "efgabcd"
# Challenge
# Rotate in-place with O(1) extra memory.

class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        n = len(str)
        offset %= n
        str[-offset:] = str[-offset:][::-1]
        str[:-offset] = str[:-offset][::-1]
        str = str[::-1]
        print str

print(Solution().rotateString(list("abcdefg"), 3))