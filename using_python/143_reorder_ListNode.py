class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        dummy = ListNode()
        dummy.next = head
        while dummy:

    def reverse(self, head: ListNode):
        if not head or not head.next:
            return head
        pre = ListNode()
        pre.next = head

        while pre and pre.next:
            tmp = pre.next
            pre.next.next = pre
            pre = temp
