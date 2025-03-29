from collections import defaultdict
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, curr_sum):
            if not node:
                return 0
            
            curr_sum += node.val
            count = paths[curr_sum - targetSum]
            
            paths[curr_sum] += 1
            
            total = count + dfs(node.left, curr_sum) + dfs(node.right, curr_sum)
            
            paths[curr_sum] -= 1
            
            return total
        
        paths = defaultdict(int)
        paths[0] = 1
        return dfs(root, 0)
