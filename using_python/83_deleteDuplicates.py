# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        pre = head
        curr = head.next
        while curr is not None and pre is not None:
            if pre.val == curr.val:
                curr = curr.next
            else:
                pre.next = curr
                pre = pre.next
                curr = curr.next
        pre.next = curr
        return head
