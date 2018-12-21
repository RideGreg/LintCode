# Give you an array of n email addresses.
# Find the number of email groups where each group has more than one email address (the address can be duplicated).
# If two strings have the same value after being transformed, they are in the same group.
#
# The rules of transforming are as follows:
# Ignore all the characters '.' before the character '@'.
# Ignore the substring which starts with the first '+'(included) and ends with the character '@'(exclude).

class Solution:
    """
    @param emails: Original email
    @return: Return the count of groups which has more than one email address in it.
    """
    def countGroups(self, emails):
        import collections
        lookup = collections.defaultdict(int)
        ans = 0
        for e in emails:
            name, domain = e.split('@')
            name = name.split('+')[0]
            after = name.replace('.', '')+'@'+domain
            if lookup[after] == 1:
                ans += 1
            lookup[after] += 1
        return ans

print(Solution().countGroups(["abc.bc+c+d@jiuzhang.com", "abcbc+d@jiuzhang.com", "abc.bc.cd@jiuzhang.com"])) # 1
print(Solution().countGroups(["abc.b+c+d@jiuzhang.com", "abcbc+d@jiuzhang.com", "abc.bc.cd@jiuzhang.com"])) # 0
