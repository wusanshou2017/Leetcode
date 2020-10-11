# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from typing import List
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    	def buildMytree(preleft,preright,inleft,inright):
            if preleft>preright:
                return None

            pre_root = preleft

            inorder_root = index[preorder[pre_root]]
            root = TreeNode(preorder[pre_root])
            size_left_subtree = inorder_root -inleft
            root.left = buildMytree(preleft+1,preleft+size_left_subtree,inleft,inright)
            root.right = buildMytree(preleft+size_left_subtree+1,preright,inorder_root+1,inright)

            return root
        n = len(preorder)
        index = {e:i for i,e in enumerate(inorder)}
        return buildMytree(0,n-1,0,n-1)


    def buildTree2(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    	if not preorder or not inorder:
    		return
    	root = TreeNode(preorder[0])
    	idx = inorder.index(preorder[0])
    	root.left = self.buildTree2(preorder[1:1+idx],inorder[:idx])
    	root.right = self.buildTree2(preorder[1+idx:],inorder[idx+1:])
    	return root











