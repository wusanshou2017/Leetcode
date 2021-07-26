class ListNode:
    def __init__(val):
        self.val = val
        self.Next = None


class Solution(object):
    """docstring for Solution"""

    def __init__(self, arg):
        super(Solution, self).__init__()
        self.arg = arg

    def sortedListToBST(head):
        if not head:
            return None

        if head.Next == None:
            return head

        pre = head
        slow = head
        fast = head
        #  find the mid node in the ListNode
        while
