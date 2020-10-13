class Solution():
    def connect(self,root:'Node')->'Node':
        if not root:
            return 
        if root.left:
            root.left.next = root.right
            if root.next :
                root.right.next =root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root

    def connect2(self,root:'Node')->'Node':
        if not root:
            return 
        first =root
        while first:
            cur =first
            while cur and cur.left:
                cur.left.next =cur.right
                if cur.next:
                    cur.right.next =cur.next.left
                cur =cur.next
            first=first.left
        return root


