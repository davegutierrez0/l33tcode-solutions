# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def maximumTraversalRecursive(root) -> int:

            if not root:
                return 0 

            left_depth = maximumTraversalRecursive(root.left)
            right_depth = maximumTraversalRecursive(root.right)
            
            return max(left_depth, right_depth) + 1

        return maximumTraversalRecursive(root)
    
    
# Time Complexity O(n)
# Space Complexity O(height)