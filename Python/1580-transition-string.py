# Give a startString, an endString, ask if you can transfer from start to end through a series of
# independent transformations. The rule is to have only 26 lowercase letters, and only one type of
# letter can be changed per operation. For example, if you change a to b, then all a in the start string
# must be b. For each type of character you can choose to convert or not convert, the conversion must be
# conducted between one character in startString and one character in endString. Return true or false.

# Solution: False in 3 cases: a. start/end have different length
# b. same char in start maps to different char in end
# c. end is a permutation of start

class Solution:
    def canTransfer(self, start, end):
        if len(start) != len(end):
            return False

        lookup, cntStart, cntEnd = {}, [0] * 26, [0] * 26
        for i in range(len(start)):
            if start[i] in lookup and lookup[start[i]] != end[i]:
                return False
            lookup[start[i]] = end[i]
            cntStart[ord(start[i]) - ord('a')] += 1
            cntEnd[ord(end[i]) - ord('a')] += 1

        return cntStart != cntEnd

print(Solution().canTransfer("abc", "cde")) # True
print(Solution().canTransfer("abc", "bca")) # False
print(Solution().canTransfer("aba", "cde")) # False
print(Solution().canTransfer("abc", "cac")) # True