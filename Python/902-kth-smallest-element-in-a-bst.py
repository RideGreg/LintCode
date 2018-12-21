# Time: O(k)
# Space: O(k)

# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
# You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

# Solution: inorder traversal, non recursive

# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: the given BST
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        stack = [(root, False)]
        while stack:
            n, visited = stack.pop()
            if not n:
                continue
            if visited:
                k -= 1
                if k == 0:
                    return n.val
            else:
                stack.append((n.right, False))
                stack.append((n, True))
                stack.append((n.left, False))

    def kthSmallest_recursive(self, root, k):
        self.ans = -1
        self.k = k

        def inorder(root):
            if not root: return

            inorder(root.left)
            self.k -= 1
            if self.k == 0:
                self.ans = root.val
            inorder(root.right)

        inorder(root)
        return self.ans