from collections import deque
from typing import List
from collections import deque
class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val =val
        self.left = left
        self.right =right

class Solution:
    def right_view(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        layer = deque()
        layer.append(root)
        res = []
        while layer:
            cur_layer = []
            for _ in range(len(layer)):
                node = layer.popleft()
                cur_layer.append(node.val)
                if node.left:
                    layer.append(node.left)
                if node.right:
                    layer.append(node.right)
            res.append(cur_layer[-1])
        return res

#  unit_test

if __name__ == '__main__':
    t1= TreeNode(1)
    t2 =TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)

    t1.left = t2
    t1.right = t3
    t2.left = t5
    t3.left =t4


    so =Solution()
    print(so.right_view(t1))

