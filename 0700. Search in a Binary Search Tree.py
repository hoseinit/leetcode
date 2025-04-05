class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(root,val):
            if root is None:
                return None
            if root.val==val:
                return root
            if root.val>val:
                return search(root.left, val)
            else:
                return search(root.right, val)
        return search(root, val)
