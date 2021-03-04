# Definition for singly-linked list.
# 输入: 4->2->1->3
# 输出: 1->2->3->4

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        sortedPtr = dummy.next
        curPtr = sortedPtr.next
        while curPtr and curPtr.next:
            temp = dummy.next
            while temp != sortedPtr.next:
                if curPtr.val < temp.val:
                    temp.val, curPtr.val = curPtr.val, temp.val

                temp = temp.next
            curPtr = curPtr.next
        return dummy.next
