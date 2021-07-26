
class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.random = None


class Solution:
    def __init__():
        self.vistedMap = {}

    def getCloneNode(self, head):
        if head:
            if head in self.vistedMap:
                return self.vistedMap[head]
            else:

                self.vistedMap[head] = Node(head.val, None, None)

                return self.vistedMap[head]
        return None

    def copyRandomList(self, head):

        if not head:
            return head

        old_node = head
        new_node = Node(head.val, None, None)
        self.vistedMap[old_node] = new_node
        while old_node != None:

            new_node.random = self.getCloneNode(old_node.random)
            new_node.next = self.getCloneNode(old_node.next)

            old_node = old_node.next
            new_node = new_node.next
        return vistedMap[head]
