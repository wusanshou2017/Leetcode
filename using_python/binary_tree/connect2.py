# [1,2,3,4,null,null,5]
# [1,2,3,4,5,null,6,7,null,null,null,null,8]

class Solution():
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return

        if root.left and root.right:
            root.left.next = root.right
            #  some flaws if root.right is None
            if root.next:
                if root.next.left and root.next.right:
                    root.right.next = root.next.left
                else:
                    if root.next.left:
                        root.right.next = root.next.left
                    elif root.next.right:
                        root.right.next = root.next.right
                    else:
                        root.right.next = None

        else:
            if root.left:
                if root.next:
                    if root.next.left and root.next.right:
                        root.left.next = root.next.left
                    else:
                        if root.next.left:
                            root.left.next = root.next.left
                        elif root.next.right:
                            root.left.next = root.next.right
                        else:
                            root.left.next = None
            elif root.right:
                if root.next:
                    if root.next.left and root.next.right:
                        root.right.next = root.next.left
                    else:
                        if root.next.left:
                            root.right.next = root.next.left
                        elif root.next.right:
                            root.right.next = root.next.right
                        else:
                            root.right.next = None
            else:
                pass

        self.connect(root.left)
        self.connect(root.right)
        return root

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
