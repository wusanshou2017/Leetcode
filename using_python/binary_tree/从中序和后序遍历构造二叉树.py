# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
    # 	if not inorder or not postorder:
    #         return 
    #     root = TreeNode(postorder[-1])
    #     idx = inorder.index(postorder[-1])
    #     root.left = self.buildTree(inorder[:idx],postorder[:idx])
    #     root.right = self.buildTree(inorder[idx+1:],postorder[idx:-1])
    #     return root

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
		def buildMytree(postleft,postright,inleft,inright):
			if postleft>postright:
				return None

			root_index = index[postorder[postright]]
			root  = TreeNode (postorder[postright])
			left_subTree_size = root_index - inleft
			root.left = buildMytree(postleft,postleft+left_subTree_size-1,inleft,inright)
			root.right = buildMytree(root_index+1,postright,root_index+1,inright)

			return root
		n = len(inorder)
		index = {e:i for i,e in enumerate(inorder)}
		return buildMytree(0,n-1,0,n-1)


