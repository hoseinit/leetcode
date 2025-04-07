class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findMin(root):
            while root.left:
                root = root.left
            return root
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                minNode = findMin(root.right)
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
            return root
        return root
