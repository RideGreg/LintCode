# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

class Solution:
    def isValidParentheses(self, s):
        stack = []
        match = {'(':')', '[':']', '{':'}'}
        for c in s:
            if c in match:
                stack.append(c)
            else:
                if not stack or match[stack.pop()] != c:
                    return False
        return not stack

print(Solution().isValidParentheses("()[]{}")) # True
print(Solution().isValidParentheses("([)]")) # False
