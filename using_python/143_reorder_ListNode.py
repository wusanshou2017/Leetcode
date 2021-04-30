# 给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
# 将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        
        # reverse_head = self.reverse(head)
        temp = head
        n = 0

        dummy = ListNode()
        while temp:
            n += 1
            print("temp.val:...", temp.val)
            temp = temp.next
        h1 = head
        dummy.next = h1

        h2 = reverse_head
        if n % 2 == 0:
            edge = n / 2
            while edge > 0:
                temp1 = h1.next
                h1.next = h2
                temp2 = h2.next
                h2.next = temp1
                h1 = temp1
                h2 = temp2
                edge -= 1
            return dummy.next

        else:

            edge = n / 2
            while edge > 1:
                temp1 = h1.next
                h1.next = h2
                temp2 = h2.next
                h2.next = temp1
                h1 = temp1
                h2 = temp2
                edge -= 1
            h2.next = h1
            return dummy.next

    def reverse(self, head: ListNode):
        dummy = ListNode()
        dummy.next = head
        pre, cur = None, head
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre


if __name__ == '__main__':
    L1 = ListNode(1)
    L2 = ListNode(2)
    L3 = ListNode(3)
    L4 = ListNode(4)
    # L5 = ListNode(5)
    L1.next = L2
    L2.next = L3
    L3.next = L4
    # L4.next = L5
    so = Solution()

    res = so.reorderList(L1)
    while res:
        print(res.val)
        res = res.next
