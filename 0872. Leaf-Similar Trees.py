class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        
        # get the leaves of both trees
        leaves1 = []
        leaves2 = []
        self.getLeaves(root1, leaves1)
        self.getLeaves(root2, leaves2)
        # compare the leaves
        return leaves1 == leaves2

    def getLeaves(self, root, leaves):
        if not root:
            return
        if not root.left and not root.right:
            leaves.append(root.val)
        self.getLeaves(root.left, leaves)
        self.getLeaves(root.right, leaves)
