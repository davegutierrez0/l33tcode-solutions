# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        targetSum -= root.val # Always subtract the head

        if not root.left and not root.right: # Leaf if it has no right and no left
            return targetSum == 0 # Must equal 0 exactly
        
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right, targetSum) # Recursively dig deeper


# 🍂 Leaf Check: PathSum = target - root.val at every level
# ✅ Return True if any root-to-leaf path adds up exactly
# Time Complexity: O(N)
# Space Complexity: O(H)