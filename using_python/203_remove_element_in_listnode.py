class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return

        pre = head
        cur = head.next
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre

    def removeElement(self, head: ListNode, target: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        cur = head
        while cur:
            if cur.val == target:
                pre.next = cur.next
            else:
                pre = cur

            cur = cur.next

        return dummy.next


def unit_test():
    nodes_lst = [ListNode(i) for i in range(10)]
    for i in range(9):
        nodes_lst[i].next = nodes_lst[i + 1]
    head = nodes_lst[0]
    so = Solution()
    res_head = so.removeElement(head, 3)
    while res_head:
        print(res_head.val)
        res_head = res_head.next


unit_test()
