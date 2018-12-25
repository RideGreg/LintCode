# Time: O(n*l), where n is # of strings in list, l is length of longest string
# Space: O(n*l)

# The distance between the two binary strings is the sum of the lengths of the common prefix removed.
# For example: the common prefix of 1011000 and 1011110 is 1011, distance is len ("000" + "110") = 3 + 3 = 6.
# Now give a list of binary strings, find max distance.

class BinaryTrieNode(object):
    def __init__(self):
        self.isString = False
        self.left = None
        self.right = None

class Trie(object):
    def __init__(self):
        self.root = BinaryTrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c == '0':
                if not cur.left:
                    cur.left = BinaryTrieNode()
                cur = cur.left
            else:
                if not cur.right:
                    cur.right = BinaryTrieNode()
                cur = cur.right
        cur.isString = True


class Solution:
    def getAns(self, s):
        def getDepth(root):
            if root is None:
                return 0

            leftDepth = getDepth(root.left)
            rightDepth = getDepth(root.right)

            if root.left and root.right:
                self.ans = max(self.ans, leftDepth + rightDepth)

            if root.left and root.isString:
                self.ans = max(self.ans, leftDepth)
            if root.right and root.isString:
                self.ans = max(self.ans, rightDepth)

            return max(leftDepth, rightDepth) + 1

        trieObj = Trie()
        for word in s:
            trieObj.insert(word)

        self.ans = 0
        getDepth(trieObj.root)
        return self.ans


print(Solution().getAns(["011000","0111010","01101010"])) # 9
print(Solution().getAns(["011000","0111011","01001010"])) # 11
