class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, maxValue):
            if not node:
                return 0
            
            res = 1 if node.val >= maxValue else 0
            maxValue = max(maxValue, node.val)
            res += dfs(node.left, maxValue)
            res += dfs(node.right, maxValue)
            return res

        return dfs(root, root.val)
