# Given a string target and a string array s, output all strings containing target(ie target is a subsequence
# of s[i]) in their original order in the array s

class Solution:
    def getAns(self, target, s):
        def isSubsequence(target, s):
            i, j = 0, 0
            while i < len(s) and j < len(target):
                if s[i] == target[j]:
                    j += 1
                i += 1
            return j == len(target)

        return [word for word in s if isSubsequence(target, word)]

print(Solution().getAns("google", ["goooogle","abc","google","higoogle","googlg","gowogwle","gogle"]))
# ["goooogle","google","higoogle","gowogwle"]))
