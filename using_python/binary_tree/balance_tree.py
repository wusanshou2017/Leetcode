class Soluiton():
    def isBalanced(self, root: TreeNode) -> bool:
        def maxDepth(root):
            if not root:
                return 0
            else:
                left_height = maxDepth(root.left)
                right_height = maxDepth(root.right)

            return max(left_height, right_height) + 1
        if not root:
            return True
        return abs(maxDepth(root.left) - maxDepth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
