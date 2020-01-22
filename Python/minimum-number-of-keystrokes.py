'''

1586. Minimum Number Of Keystrokes
Given an English word that contains only uppercase and lowercase letters, ask at least a few keystrokes to enter the word (you can press caps lock and shift, and initially enter lowercase letters by default).

Example
Give s="Hadoop", return 7

Explanation:
Hold down the Shift key and then h to enter H, then press adoop in turn to enter.
Give s="HADOOp",return 8

Explanation:
First press caps lock, press hadoo, then caps lock, and finally press p.
Notice
The length of the word does not exceed 200000200000
'''

class Solution:
    """
    @param s: the English word
    @return: The number of keystrokes
    """
    def getAns(self, s):
        n, ans, i = len(s), 0, 0
        while i < n:
            if 'a'<=s[i]<='z':
                ans += 1
                i += 1
            else:
                j = i
                while j<n and 'A'<=s[j]<='Z':
                    j += 1
                if j-i == 1:
                    ans += (j-i+1)
                else:
                    ans += (j-i+1 if j == n else j-i+2)
                i = j
        return ans

print(Solution().getAns("EWlweWXZXxcscSDSDcccsdcfdsFvccDCcDCcdDcGvTvEEdddEEddEdEdAs")) #78
print(Solution().getAns("EWlweWXZXxcscSDSDcccsdcfdsFvccDCcDCcdDcGvTv")) #57
print(Solution().getAns("dhsKGHJAHgSgssSgkBghgbbHJGJjdgjgABAJGJbbjbbnBBbbBBBBBBBBBBBBBBBBBBBBBbAAAAAAAAAAjhdjkdhjkSSSXxxbjmnAa")) #118
print(Solution().getAns("SFDSFdsfdvsdffvSDFGFSDgvfdvsfgvSDFGVFDbvfdbfbdfbVDFfffbgdfgdfgVDddddddBdbdbxvggeAAddAAAAxxxAAssssd")) #115
#                                            26                                      70                          106
print(Solution().getAns('Hadoop')) #7
print(Solution().getAns('HADOOp')) #8
print(Solution().getAns('H')) #2
print(Solution().getAns('p')) #1
print(Solution().getAns('')) #0
