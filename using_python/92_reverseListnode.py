# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None

        pre,cur = None, head
        for _ in range (m-1):
            pre=cur 
            cur = cur.next

        conn,tail = pre,cur 

        for _ in range (n-m+1):
            temp = cur.next
            cur.next  = pre
            pre =cur 
            cur =temp

        if conn:
            conn.next=pre
        else:   
            head=pre
        tail.next=cur
        return head 