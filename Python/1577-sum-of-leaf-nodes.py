# -*- encoding: utf-8 -*-

# Time: O(n)
# Space: O(1)

# Given a binary tree, find the sum of all leaf nodes. Use O(1) space, i.e. no recursion or stack.

# Morris inorder traversal, 利用二叉树中叶节点的right指针来保存接下来要访问的节点，这个right指针使用完成后再重置为None。
# 不使用递归或栈，空间复杂度O(1)。
class Solution:
    def sumLeafNode(self, root):
        res = 0

        cur = root
        while cur:
            if cur.left is None:
                if cur.right is None:  # cur is a leaf node
                    res += cur.val
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                if prev.right is None:
                    if prev.left is None:  # prev is a leaf node
                        res += prev.val
                    prev.right = cur
                    cur = cur.left
                else:
                    prev.right = None
                    cur = cur.right
        return res

        ''' recursive
        def re(root, v):
            if not root: return v
            if not root.left and not root.right:
                return v + root.val
            v = re(root.left, v)
            v = re(root.right, v)
            return v

        return re(root, 0)
        '''

        ''' iteration
        ans = 0
        stack = [(root, False)]
        while stack:
            cur, visited = stack.pop()
            if not cur: continue
            if visited:
                if not cur.left and not cur.right:
                    ans += cur.val
            else:
                stack.append((cur.right, False))
                stack.append((cur, True))
                stack.append((cur.left, False))

        return ans
        '''
class TreeNode(object):
    def __init__(self, n):
        self.val = n
        self.left = None
        self.right = None

root = TreeNode(1)
root.left, root.right = TreeNode(2), TreeNode(3)
root.left.left, root.left.right = TreeNode(4), TreeNode(5)
print(Solution().sumLeafNode(root)) # 12