# Definition for singly-linked list.
# 输入: 4->2->1->3
# 输出: 1->2->3->4

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(float("-inf"))
        dummy.next = head
        sortedPtr = dummy
        curPtr = sortedPtr.next
        # while curPtr :
        #     temp = sortedPtr.next                       
        #     while sortedPtr and temp != sortedPtr.next:
        #         if curPtr.val < temp.val:
        #             temp.val, curPtr.val = curPtr.val, temp.val
        #             sortedPtr = sortedPtr.next
        #         temp = temp.next
        #     curPtr = curPtr.next
        
        while curPtr:
            temp =dummy
            while temp!=sortedPtr.next:
                if temp.val>curPtr.val:
                    curPtr.val ,temp.val = temp.val,curPtr.val
                temp=temp.next

            curPtr=curPtr.next
            sortedPtr =sortedPtr.next

        return dummy.next


# unit_test

if __name__ == '__main__':
    l1 =ListNode(3)
    l2 = ListNode(1)
    l3 =ListNode(2)
    l4 =ListNode(4)
    l5 = ListNode(0)
    l1.next=l2
    l2.next=l3
    l3.next =l4
    l4.next=l5
    so =Solution()

    res =so.insertionSortList(l1)
    while res:
        print(res.val)
        res =res.next