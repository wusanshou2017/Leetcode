# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head 

        dummy = ListNode(0)
        dummy.next = head

        slow,fast = dummy,dummy
        for _ in range(m-1):
            fast=fast.next
        for _ in range(n-1):
            slow =slow.next

        slow_head, fast_head =  slow.next,fast.next

        pre =slow_head
        cur = slow_head.next
        while cur!= fast_head:
            cur_next = cur.next
            cur_next.next=pre
            pre =cur 
            cur =cur_next

        slow.next = cur
        fast.next =fast_head
        return dummy.next

