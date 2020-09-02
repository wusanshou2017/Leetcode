# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # 对象的直接赋值 是引用
        dummy = pre = ListNode(0)
        dummy.next = head

        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head

            else:
                head = head.next
                pre = pre.next
        return dummy.next

    def remove_duplicates(self, head: ListNode) -> ListNode:
        dummy = pre = ListNode(0)
        dummy.next = head
        # not end node
        while head and head.next:
            if head.val == head.next.val:
                while head.val == head.next.val and head and head.next:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                head = head.next
                pre = pre.next

        return dummy.next
