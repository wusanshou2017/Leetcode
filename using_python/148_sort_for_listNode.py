# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head.next:
            return []
        pre = head.val
        dummy = head
        while dummy.next:
            pre = dummy.val
            cur = dummy.next.val
            if cur < pre:
                dummy.val, dummy.next.val = cur, pre

    def cut(self, head: ListNode) -> ListNode:

        P = head
        while (n - 1) and p:
            p = p.next
            n -= 1
        if not p:
            return None

        ce = p.next
        ce.next = None
        return ce

    def merge(seq1, seq2):
        dummy = ListNode()
