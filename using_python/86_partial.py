class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 输入: head = 1->4->3->2->5->2, x = 3
# 输出: 1->2->2->4->3->5
class Solution(object):
    def partition(self, head, x):
       
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
           
            if head.val < x:
                before.next = head
                before = before.next
            else:
             
                after.next = head
                after = after.next

           
            head = head.next

        
        after.next = None
       
        before.next = after_head.next

        return before_head.next

    def my_solution(self,head,x):
        dummy1 = dummy1_head = ListNode(0)
        dummy2 = dummy2_head =ListNode(0)
        while head:
            if head.val<x:
                dummy1.next=head
                dummy1=dummy1.next
            else:
                dummy2.next=head
                dummy2= dummy2.next

            head =head.next

        dummy1.next = dummy2_head.next
        dummy2.next =None 

        return dummy1_head.next