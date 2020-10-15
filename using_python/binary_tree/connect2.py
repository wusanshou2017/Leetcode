# [1,2,3,4,null,null,5]
# [1,2,3,4,5,null,6,7,null,null,null,null,8]

class Solution():
    def connect2(self, root: 'Node') -> 'Node':
        dummy_left_node = Node()
        pre = dummy_left_node
        current_node = root

        while current_node:
            if current_node.left:
                pre.next = current_node.left
                pre = pre.next
            if current_node.right:
                pre.next = current_node.right
                pre = pre.next

            current_node = current_node.next

            if not current_node:
                current_node = dummy_left_node.next
                dummy_left_node.next = None
                pre = dummy_left_node
        return root


class Solution {
    public:
    void handle(Node * &last, Node * &p, Node * &nextStart) {
        if (last) {
            last -> next = p; }
        if (!nextStart) {
            nextStart = p; }
        last = p; }

    Node * connect(Node * root) {
        if (!root) {
            return nullptr; }
        Node * start = root;
        while (start) {
            Node * last = nullptr, *nextStart = nullptr;
            for (Node * p=start; p != nullptr; p=p -> next) {
                if (p -> left) {
                    handle(last, p -> left, nextStart); }
                if (p -> right) {
                    handle(last, p -> right, nextStart); }
            }
            start = nextStart; }
        return root; }
};

    def connect3(self , root:'Node')->'Node':
        if not root:
            return None
        start = root
        while start:
            last = None
            q = None
            for 

    def helper(self,last,p,q):
        if last:
            last.next = p
        if not q:
            q =p
        last =p
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        dummy = Node()
        pre = dummy
        first = root 
        while first:
            if first.left:
                pre.next = first.left
                pre = pre.next
            if first.right:
                pre.next = first.right
                pre = pre.next

            first = first.next
            if not first:
                first= dummy.next
                dummy = Node()
                pre = dummy
        return root 
