# Given a linked list, swap every two adjacent nodes and return its head.
#
# Example
# Given 1->2->3->4, you should return the list as 2->1->4->3.
#
# Challenge
# Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: a ListNode
    @return: a ListNode
    """
    def swapPairs(self, head):
        # k组翻转链表的简单版. 它没有给真正意义的头指针, 核心思想建立一个dummy node为头指针, 然后3部曲进行交换
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            slow, fast = prev.next, prev.next.next
            slow.next = fast.next
            fast.next = slow
            prev.next = fast
            prev = slow
        return dummy.next

    def swapPairs_recur(self, head):
        if not head or not head.next:
            return head
        slow, fast = head, head.next
        slow.next = self.swapPairs(fast.next)
        fast.next = slow
        return fast

    def swapPairs_switchValue(self, head):
        slow = head
        while slow and slow.next:
            fast = slow.next
            fast.val, slow.val = slow.val, fast.val
            slow = fast.next
        return head

    def swapPairs_buildNewList(self, head):
        dummy = ListNode(0)
        cur = dummy

        slow = head
        while slow:
            fast = slow.next
            if fast:
                cur.next = ListNode(fast.val)
                cur = cur.next
            cur.next = ListNode(slow.val)
            cur = cur.next

            if fast:
                slow = fast.next
            else:
                break
        return dummy.next