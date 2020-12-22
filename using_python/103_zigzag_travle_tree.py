# Definition for a binary tree node.
from typing import List
from collections import deque
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return [[]]

        flag_level = True

        result,queue = [], deque([root])
        while queue:
            level_len =len(queue)
            level_nodes = []
            while level_len > 0:
                
                cur_node = queue.popleft() 
                level_nodes.append(cur_node.val)
               
                if cur_node.right:
                    queue.append(cur_node.right)
                if cur_node.left:
                    queue.append(cur_node.left)                    
                
                level_len-=1
            if flag_level:
                result.append(level_nodes[:])
            else:
                result.append(level_nodes[::-1])
            flag_level = not flag_level
        return result


# input : [3,9,20,null,null,15,7]
# expect_output: [[3],[20,9],[15,7]]




