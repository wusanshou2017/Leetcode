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
        pre = head
        cur = head.next

        while cur:
            tmp = cur.next
            cur.next= pre
            pre =cur
            cur =temp 
        return pre 
