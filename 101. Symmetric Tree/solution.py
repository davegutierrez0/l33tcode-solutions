# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def symmetryCheck(left,right):
            if left is None and right is None:
                return True
            if left is None or right is None:
                return False
            return (
                (left.val == right.val) 
                and symmetryCheck(left.left,right.right)
                and symmetryCheck(left.right,right.left)
                )


        return symmetryCheck(root,root)


# Time Complexity: O(N)
# Space Complexity: O(H)# Think: "Mirror Match"
# Check (1) Value Equality, (2) Cross Children:
# left.left <--> right.right
# left.right <--> right.left
# Has to be True for both pairs and value equality.
# 🪞 #MirrorLogic: L.left <-> R.right AND L.right <-> R.left
# ✅ #BaseCase: both None = True, one None = False