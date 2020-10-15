# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # visited =[]
        # while head and head.next:
        #     head=head.next
        #     if head not in visited:
        #         visited.append(head)
        #     else:
        #         return True
        
        # return False 

        if not head or not head.next:
            return False

        slow = head
        fast =head.next 
        while slow!=fast:
            if not fast or not fast.next:
                return False
            slow =slow.next
            fast = fast.next.next

        return True  