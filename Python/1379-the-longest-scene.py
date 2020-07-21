# 1379
# A string, each character representing a scene. Between two identical characters is considered
# to be a continuous scene. For example: abcda, you can think of these five characters as the same scene.
# Or acafghbeb can think of two aca and beb scenes.
#
# If there is a coincidence between the scenes, then the scenes are combined. For example, abcab,
# where abca and bcab are coincident, then the five characters are considered to be the same scene.
#
# Give a string to find the longest scene.
#
# Note: 1 <= |str| <=1e5, str contains only lowercase letters

# 扫描线：记录每个字符的左端点和右端点，相等于求若干线段合并后最长线段长度，使用扫描线即可。时间复杂度O(n)

import collections
class Solution:
    """
    @param str: The scene string
    @return: Return the length longest scene
    """
    def getLongestScene(self, str):
        seg = [[len(str), -1] for _ in range(26)] # [firstPosition, lastPosition]
        for i in range(len(str)):
            t = ord(str[i]) - ord('a')
            seg[t][0] = min(seg[t][0], i)
            seg[t][1] = max(seg[t][1], i)
        seg.sort()

        # merge interval
        ans = seg[0][1] - seg[0][0] + 1
        l, r = seg[0]
        for i in range(len(seg)):
            if seg[i][0] < len(str) and seg[i][1] >= 0 :
                if seg[i][0] <= r:
                    r = max(r, seg[i][1])
                else:
                    l, r = seg[i]
                ans = max(ans, r - l + 1)
        return ans

print(Solution().getLongestScene("abcda")) # 5
print(Solution().getLongestScene("abcab")) # 5
